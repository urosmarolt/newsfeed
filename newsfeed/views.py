from django.views.generic import DetailView, ListView
from .models import EventregistryPost
from twitter import *
from django.conf import settings
from constance import config
from django.db.models import Count

from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

class PostList(ListView):
    model = EventregistryPost
    context_object_name = "posts"
    template_name = "posts.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['tweeter_feeds'] = get_twetter_feed()
        try:
            page = int(self.request.GET.get('page'))
        except:
            page = 1

        #pagination parameters - page_numbers range
        adjacent_pages = 3
        context['page_numbers'] = [n for n in \
                        range(page - adjacent_pages, page + adjacent_pages + 1) \
                        if n > 0 and n <= page]
        if 1 not in context['page_numbers']:
            context['show_first'] = True
        if page not in context['page_numbers']:
            context['show_last'] = True


        return context

class PostDetail(DetailView):
    model = EventregistryPost
    context_object_name = "post_detail"
    template_name = "post_detail.html"

class SourceList(ListView):
    model = EventregistryPost
    context_object_name = "sources"
    template_name = "source_list.html"
    queryset = EventregistryPost.objects.values('source_title', 'source_id').annotate(Count('source_title')).order_by('-source_title__count', 'source_title')

    def get_context_data(self, **kwargs):
        context = super(SourceList, self).get_context_data(**kwargs)
        context['tweeter_feeds'] = get_twetter_feed()
        return context

class SourcePostList(ListView):
    model = EventregistryPost
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        # original queryset filtered by a variable captured from url ['source_id']
        qs = super().get_queryset().filter(source_id=self.kwargs['source_id'])
        return qs

    """
    def get_context_data(self, **kwargs):
        context = super(SourcePostList, self).get_context_data(**kwargs)
        context['posts_by_source'] = EventregistryPost.objects.filter(source_id=self.kwargs['source_id'])
        return context
    """



def get_twetter_feed():
    try:
        # configure Twitter API
        twitter = Twitter(auth=OAuth(settings.OAUTH_TOKEN, settings.OAUTH_SECRET, settings.CONSUMER_KEY, settings.CONSUMER_SECRET))
        # search with query term and return 10
        t_results = twitter.search.tweets(q=config.TWEETER_KEYWORDS, count=10)
        return t_results.get('statuses')
    except:
        pass
