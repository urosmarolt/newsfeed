import factory
from .models import EventregistryPost

class EventRegistryPostFactory(factory.django.DjangoModelFactory):
    """
    Define EventRegistryPost factory
    """
    class Meta:
        model = EventregistryPost