#coding: utf-8
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from rss_reader.models import RSS_ReaderPlugin as RSS_ReaderPluginModel
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect

import feedparser
from django.utils.datastructures import MultiValueDictKeyError

class RSS_ReaderPlugin(CMSPluginBase):
    name = u"RSS_Reader"
    render_template = "rss_reader/lista_news.html"
    model = RSS_ReaderPluginModel


    def render(self, context, instance, placeholder):
        request = context['request']
        entries = feedparser.parse(instance.url_page)["entries"]
        query=""
        news_date=""
        news_title=""
        news_content=""
        try:
            query = request.GET["entry"]
            for o in entries:
                if query == o["link"].replace("http://news.santacruzfc-pe.com.br/index.php/","").replace("/",""):
                    news_date=str(o["updated_parsed"].tm_mday)+"/"+str(o["updated_parsed"].tm_mon)+"/"+str(o["updated_parsed"].tm_year)+" "+str(o["updated_parsed"].tm_hour)+":"+str(o["updated_parsed"].tm_min)
                    news_title=o["title"]
                    news_content=o["content"][0]["value"]
                    
                    
		    
        except MultiValueDictKeyError as erro:
            print erro
        
        teste=entries[0]["updated_parsed"][0]
        
        context.update({
            "qrystr" :  query,
            "news_date" :  news_date,
            "news_title" : news_title,
            "news_content" : news_content,
            "teste" : teste,
            'entries': entries,
        })
        return context
plugin_pool.register_plugin(RSS_ReaderPlugin) # register the plugin 



