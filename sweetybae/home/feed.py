from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from product.models import fruits
from django.urls import reverse
from django.shortcuts import redirect


class latest(Feed):
    title='sweetybae'
    link='/drcomments/'
    description='A well arranged selection of fruits'


    def items(self):
        return fruits.objects.all()[:5]
    def item_description(self,data):
        return truncatewords(data.des,10)
    def item_link(self,data):
        return reverse('homepage')