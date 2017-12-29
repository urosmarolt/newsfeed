from eventregistry import *
import re
import redis
import sys
import os
import django
from urllib.parse import urlparse



sys.path.append('/Users/uros.marolt/Documents/docker/aggregator/aggregator')
os.environ['DJANGO_SETTINGS_MODULE'] = 'aggregator.settings'
django.setup()
from newsfeed.models import EventregistryPost
redis_url = urlparse(os.getenv('REDIS_URL'))
print(redis_url.password)
try:
    POOL = redis.ConnectionPool(host=redis_url.hostname, port=redis_url.port, db=0, password=redis_url.password)
    print('Connected!')
except Exception as ex:
    print('Error:', ex)
    exit('Failed to connect, terminating.')

def getVariable(variable_name):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(variable_name)
    print(response)
    return re.search(r'\[(.*)\]', str(response)).group(1)


def pullItems():

    er = EventRegistry()


    category = er.getCategoryUri("news")
    keyword_items = QueryItems.OR([getVariable('constance:EVENTREGISTRY_QUERY')])
    q = QueryArticles(keywords=keyword_items, lang="eng")

    res = er.execQuery(q)
    q.setRequestedResult(RequestArticlesInfo(count=50,
                                             returnInfo=ReturnInfo(
                                                 articleInfo=ArticleInfoFlags(duplicateList=True, concepts=False,
                                                                              categories=False, location=False,
                                                                              image=True))))

    for item in res['articles']['results']:
        try:
            if item["isDuplicate"] == True:
                del item
            else:
                #cleanup dict raw data structure
                del item["uri"]
                del item["lang"]
                del item["dateTime"]
                del item["eventUri"]
                del item["wgt"]
                del item["sim"]
                del item["isDuplicate"]

                item["sourceID"] = item["source"]["id"]
                item["sourceUrl"] = item["source"]["uri"]
                item["sourceTitle"] = item["source"]["title"]

                #remove off characters, lowercase string and replace spaces with -
                str = re.sub("['.:;\"()/?!|´]", '', item["title"].lower())
                item["postUrl"] = str.replace(' ', '-')
                del item["source"]
                item["datetime"] = item["date"] + " " + item["time"]
                del item["date"]
                del item["time"]

                item["tags"] = getVariable('constance:EVENTREGISTRY_QUERY')



                eventRegistryItem = EventregistryPost()

                eventRegistryItem.news_id = item["id"]
                eventRegistryItem.source_id = item["sourceID"]
                eventRegistryItem.source_url = item["sourceUrl"]
                eventRegistryItem.source_title = item["sourceTitle"]
                eventRegistryItem.title = item["title"]
                eventRegistryItem.body = item["body"]
                eventRegistryItem.url = item["url"]
                eventRegistryItem.slug = item["postUrl"]
                eventRegistryItem.created_at = item["datetime"]
                eventRegistryItem.tags = item["tags"]

                print(eventRegistryItem)
                try:
                    eventRegistryItem.save()
                except Exception as e:
                    print("Error \n %s" % (e))

                #saveToDB(item)

        except Exception as e:
            print("Error \n %s" % (e))

pullItems()