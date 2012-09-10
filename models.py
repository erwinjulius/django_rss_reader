# coding: utf-8
from django.db import models
from cms.models import CMSPlugin


class RSS_ReaderPlugin(CMSPlugin):
    url_page = models.CharField("origem", max_length=300)

    def __unicode__(self):
      return 'RSS de %s' % self.url_page
