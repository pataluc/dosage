# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2013 Bastian Kleineidam

from re import compile, escape, IGNORECASE

from ..scraper import _BasicScraper
from ..util import tagre


class MacHall(_BasicScraper):
    url = 'http://www.machall.com/'
    stripUrl = url + 'view.php?date=%s'
    firstStripUrl = stripUrl % '2000-11-07'
    imageSearch = compile(r'<img src="(comics/.+?)"')
    prevSearch = compile(r'<a href="(.+?)"><img[^>]+?src=\'drop_shadow/previous.gif\'>')
    help = 'Index format: yyyy-mm-dd'


# broken links - disable for now
class MadamAndEve(_BasicScraper):
    url = 'http://www.madamandeve.co.za/week_of_cartns.php'
    stripUrl = None
    imageSearch = compile(r'<IMG BORDER="0" SRC="(cartoons/me\d{6}\.(gif|jpg))">')
    prevSearch = compile(r'<a href="(weekend_cartoon.php)"')
    multipleImagesPerStrip = True


class MagickChicks(_BasicScraper):
    url = 'http://www.magickchicks.com/'
    stripUrl = url + 'strips-mc/%s'
    firstStripUrl = stripUrl % 'tis_but_a_trifle'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-mc/[^"]+)', before="cn[id]prevt"))
    help = 'Index format: name'


class ManlyGuysDoingManlyThings(_BasicScraper):
    description = u'Manly Guys Doing Manly Things \xbb Updated Mondays or whenever I feel like it'
    url = 'http://thepunchlineismachismo.com/'
    rurl = escape(url)
    stripUrl = url + 'archives/comic/%s'
    firstStripUrl = stripUrl % '02222010'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d+-\d+-\d+[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%sarchives/comic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: ddmmyyyy'


class Marilith(_BasicScraper):
    url = 'http://www.marilith.com/'
    stripUrl = url + 'archive.php?date=%s'
    firstStripUrl = stripUrl % '20041215'
    imageSearch = compile(r'<img src="(comics/.+?)" border')
    prevSearch = compile(r'<a href="(archive\.php\?date=.+?)"><img border=0 name=previous_day')
    help = 'Index format: yyyymmdd'


class Meek(_BasicScraper):
    url = 'http://www.meekcomic.com/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % '2008/12/27/chapter-1-cover '
    imageSearch = compile(r'meekcomic.com(/comics/.+?)"')
    prevSearch = compile(r'\s.+?(http://www.meekcomic.com/.+?)".+?Previous<')
    help = 'Index format: yyyy/mm/dd/ch-p/'


class MegaTokyo(_BasicScraper):
    url = 'http://megatokyo.com/'
    stripUrl = url + 'strip/%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(r'"(strips/.+?)"', IGNORECASE)
    prevSearch = compile(r'"(./strip/\d+?)">Prev')
    help = 'Index format: nnnn'


class Meiosis(_BasicScraper):
    url = 'http://meiosiswebcomic.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2006/10/10142006'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s[^"]+)' % rurl, after="navi-prev"))
    help = 'Index format: yyyy/mm/ddmmyyyy'


class MenageA3(_BasicScraper):
    adult = True
    url = 'http://www.ma3comic.com/'
    stripUrl = url + 'strips-ma3/%s'
    imageSearch = compile(tagre("img", "src", r'([^"]*/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'([^"]*/strips-ma3/[^"]+)', before="cn[id]prev"))
    help = 'Index format: name'


class Melonpool(_BasicScraper):
    description = u"Star Trek Meets Gilligan's Island"
    url = 'http://www.melonpool.com/'
    rurl = escape(url)
    stripUrl = url + '?p=%s'
    firstStripUrl = stripUrl % '41'
    imageSearch = compile(tagre("img", "src", r'(%scomics/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\?p=\d+)' % rurl, after="prev"))
    help = 'Index format: n'


class Misfile(_BasicScraper):
    url = 'http://www.misfile.com/'
    stripUrl = url + '?date=%s'
    firstStripUrl = stripUrl % '2004-02-22'
    imageSearch = compile(tagre("img", "src", r"(comics/[^']+)", quote="'"))
    prevSearch = compile(tagre("link", "href", r"([^']+)", quote="'", before="Previous"))
    help = 'Index format: yyyy-mm-dd'


class MyCartoons(_BasicScraper):
    url = 'http://mycartoons.de/'
    rurl = escape(url)
    stripUrl = url + 'page/%s'
    imageSearch = (
        compile(tagre("img", "src", r'(%swp-content/cartoons/(?:[^"]+/)?\d+-\d+-\d+[^"]+)' % rurl)),
        compile(tagre("img", "src", r'(%scartoons/[^"]+/\d+-\d+-\d+[^"]+)' % rurl)),
    )
    prevSearch = compile(tagre("a", "href", r'(%spage/[^"]+)' % rurl) + "&laquo;")
    help = 'Index format: number'
    lang = 'de'


class MysteriesOfTheArcana(_BasicScraper):
    url = 'http://mysteriesofthearcana.com/'
    stripUrl = url + 'index.php?action=comics&cid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(image\.php\?type=com&i=[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(index\.php[^"]+)', after="navprevious"))
    help = 'Index format: n (unpadded)'
