# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre
from ..helpers import indirectStarter


class WapsiSquare(_BasicScraper):
    url = 'http://wapsisquare.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    firstStripUrl = stripUrl % '09092001'
    imageSearch = compile(r'<img src="(%scomics/.+?)"' % rurl)
    prevSearch = compile(r'<a href="(.+?)"[^>]+?>Previous</a>')
    help = 'Index format: stripname'


class WastedTalent(_BasicScraper):
    url = 'http://www.wastedtalent.ca/'
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % 'anime-crack'
    imageSearch = compile(tagre("img", "src", r'(http://www\.wastedtalent\.ca/sites/default/files/imagecache/comic_full/comics/\d+/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/comic/[^"]+)', after="comic_prev"))
    help = 'Index format: stripname'


class WayfarersMoon(_BasicScraper):
    url = 'http://www.wayfarersmoon.com/'
    stripUrl = url + 'index.php?page=%s'
    firstStripUrl = stripUrl % '0'
    imageSearch = compile(r'<img src="(/admin.+?)"')
    prevSearch = compile(r'<a href="(.+?)".+?btn_back.gif')
    help = 'Index format: nn'


class WebDesignerCOTW(_BasicScraper):
    url = 'http://www.webdesignerdepot.com/'
    rurl = escape(url)
    starter = indirectStarter(url, compile(tagre("a", "href", r'(%s\d+/\d+/[^"]+/)' % rurl)))
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2009/11/comics-of-the-week-1'
    imageSearch = (
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/\d+/\d+/\d+s?\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/\d+/\d+/Christmas\d+\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/comics\d+[a-z0-9]*/\d+a?\.[^"]+)')),
        compile(tagre("img", "src", r'(http://netdna\.webdesignerdepot\.com/uploads/comics/\d+\.[^"]+)')),
    )
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("link", "href", r"(%s\d+/\d+/[^']+)" % rurl, before='prev', quote="'"))
    help = 'Index format: yyyy/mm/stripname'
    description = u"The content revolves around web design, blogging and funny situations that we encounter in our daily lives as designers and this week we focus on Christmas. These great cartoons are created by Jerry King, an award-winning cartoonist who’s one of the most published, prolific and versatile cartoonists in the world today."

    def shouldSkipUrl(self, url):
        """Skip non-comic URLs."""
        return 'comics-of-the-week' not in url

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        imagename = imageUrl.rsplit('/', 1)[1]
        week = compile(r'week-(\d+)').search(pageUrl).group(1)
        return "%s-%s" % (week, imagename)


class WeCanSleepTomorrow(_BasicScraper):
    description = u'We Can Sleep Tomorrow - Life does not take bathroom breaks. A webcomic that updates Mondays and Fridays'
    url = 'http://wecansleeptomorrow.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class WhiteNinja(_BasicScraper):
    baseUrl = 'http://www.whiteninjacomics.com/'
    url = baseUrl + 'comics.shtml'
    stripUrl = baseUrl + 'comics/%s.shtml'
    imageSearch = compile(r'<img src=(/images/comics/(?!t-).+?\.gif) border=0')
    prevSearch = compile(r'(/comics/.+?shtml).+?previous')
    help = 'Index format: s (comic name)'


class WhiteNoise(_BasicScraper):
    baseUrl = 'http://www.wncomic.com/'
    url = baseUrl + 'archive.php'
    stripUrl = baseUrl + 'archive_comments.php?strip_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'(istrip_files/strips/.+?)"')
    prevSearch = compile(r'</a><a href="(.+?)"><img src="images/top_back.jpg" ')
    help = 'Index format: n'


class WhyTheLongFace(_BasicScraper):
    baseUrl = 'http://www.absurdnotions.org/'
    rurl = escape(baseUrl)
    url = baseUrl + 'wtlf200709.html'
    stripUrl = baseUrl + 'wtlf%s.html'
    firstStripUrl = stripUrl % '200306'
    imageSearch = compile(r'<img src="(%swtlf.+?|lf\d+.\w{1,4})"' % rurl, IGNORECASE)
    multipleImagesPerStrip = True
    prevSearch = compile(r'HREF="(.+?)"><IMG SRC="nprev.gif" ')
    help = 'Index format: yyyymm'


class Wigu(_BasicScraper):
    description = u'WIGU: A COMIC ON INTERNET'
    url = 'http://wigucomics.com/'
    stripUrl = url + 'adventures/index.php?comic=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(/adventures/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/adventures/index\.php\?comic=\d+)', after="go back"))
    help = 'Index format: n'


class Wonderella(_BasicScraper):
    url = 'http://nonadventures.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/09/09/the-torment-of-a-thousand-yesterdays'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/name'


class Wondermark(_BasicScraper):
    url = 'http://wondermark.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '001'
    imageSearch = compile(r'<img src="(http://wondermark.com/c/.+?)"')
    prevSearch = compile(r'<a href="(.+?)" rel="prev">')
    help = 'Index format: nnn'


class WorldOfMrToast(_BasicScraper):
    baseUrl = 'http://www.theimaginaryworld.com/'
    url = baseUrl + 'mrTcomicA.html'
    stripUrl = baseUrl + '%s.html'
    imageSearch = compile(tagre("img", "src", r'(comic[^"]+)'))
    # list the archive links since there is no prev/next navigation
    prevurls = (
        url,
        baseUrl + 'mrTcomicW02.html',
        baseUrl + 'mrTcomicW01.html',
        baseUrl + 'mrGcomic03.html',
        baseUrl + 'mrGcomic02.html',
        baseUrl + 'mrGcomic01.html',
        baseUrl + 'mrTcomicT05.html',
        baseUrl + 'mrTcomicT04.html',
        baseUrl + 'mrTcomicT03.html',
        baseUrl + 'mrTcomicT02.html',
        baseUrl + 'mrTcomicT01.html',
        baseUrl + 'mrTcomicIW3.html',
        baseUrl + 'mrTcomicIW2.html',
        baseUrl + 'mrTcomicIW1.html',
    )
    firstStripUrl = prevurls[-1]
    multipleImagesPerStrip = True
    help = 'Index format: none'

    def getPrevUrl(self, url, data, baseUrl):
        idx = self.prevurls.index(url)
        try:
            return self.prevurls[idx+1]
        except IndexError:
            return None


class WormWorldSaga(_BasicScraper):
    description = u'The Wormworld Saga Online Graphic Novel by Daniel Lieske - An Epic Fantasy Adventure for all Ages'
    url = 'http://www.wormworldsaga.com/'
    stripUrl = url + 'chapters/%s/index.php'
    firstStripUrl = stripUrl % 'chapter01/EN'
    imageSearch = (
        compile(tagre("img", "src", r'(images/CH\d+_\d+\.[^"]+)')),
        compile(tagre("img", "src", r'(panels/CH\d+_[^"]+)')),
    )
    latestChapter = 5
    multipleImagesPerStrip = True

    @classmethod
    def starter(cls):
        return '%schapters/chapter%02d/%s/index.php' % (
            cls.url, cls.latestChapter, cls.lang.upper())

    def getPrevUrl(self, url, data, baseUrl):
        """Find previous URL."""
        if 'chapter04' in url:
            return url.replace('chapter04', 'chapter03')
        if 'chapter03' in url:
            return url.replace('chapter03', 'chapter02')
        if 'chapter02' in url:
            return url.replace('chapter02', 'chapter01')
        return None


class WormWorldSagaGerman(WormWorldSaga):
    lang = 'de'

class WormWorldSagaSpanish(WormWorldSaga):
    lang = 'es'

class WormWorldSagaFrench(WormWorldSaga):
    lang = 'fr'


class WotNow(_BasicScraper):
    url = 'http://shadowburn.binmode.com/wotnow/'
    stripUrl = url + 'comic.php?comic_id=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'<IMG SRC="(comics/.+?)"')
    prevSearch = compile(r'<A HREF="(.+?)"><IMG SRC="images/b_prev.gif" ')
    help = 'Index format: n (unpadded)'


# XXX disallowed by robots.txt
class _WorldOfWarcraftEh(_BasicScraper):
    url = 'http://woweh.com/'
    stripUrl = None
    imageSearch = compile(r'http://woweh.com/(comics/.+?)"')
    prevSearch = compile(r'woweh.com/(\?p=.+:?)".+:?="prev')


class Wulffmorgenthaler(_BasicScraper):
    description = u"Entertainment - Since 2002. Wulff & Morgenthaler's Personal humoristic social commentary on life, nostalgia and the World in general. Nothing is taboo: They deal with Politics, News, Entertainment, Technology, Culture, and Weirdo Beavers"
    url = 'http://wumocomicstrip.com/'
    stripUrl = url + '%s'
    imageSearch = compile(tagre("img", "src", r'(/img/strip/\d+/\d+/[^/"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]+)') + "<span>Previous")
    help = 'Index format: yyyy/mm/dd'
