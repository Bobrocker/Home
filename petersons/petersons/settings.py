# Scrapy settings for petersons project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'petersons'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['petersons.spiders']
NEWSPIDER_MODULE = 'petersons.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

#ITEM_PIPELINES = ['petersons.pipelines.FilePipeline']
