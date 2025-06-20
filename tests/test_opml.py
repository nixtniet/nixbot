# This file is placed in the Public Domain.


"no tests"


import unittest


from nixbot.modules.rss import OPML


TXT = """<opml version="1.0">
    <head>
        <title>Sample OPML file for RSSReader</title>
    </head>
    <body>
        <outline title="News" text="News">
            <outline text="Big News Finland" title="Big News Finland" type="rss" xmlUrl="http://www.bignewsnetwork.com/?rss=37e8860164ce009a"/>
            <outline text="Euronews" title="Euronews" type="rss" xmlUrl="http://feeds.feedburner.com/euronews/en/news/"/>
            <outline text="Reuters Top News" title="Reuters Top News" type="rss" xmlUrl="http://feeds.reuters.com/reuters/topNews"/>
            <outline text="Yahoo Europe" title="Yahoo Europe" type="rss" xmlUrl="http://rss.news.yahoo.com/rss/europe"/>
        </outline>

        <outline title="Leisure" text="Leisure">
            <outline text="CNN Entertainment" title="CNN Entertainment" type="rss" xmlUrl="http://rss.cnn.com/rss/edition_entertainment.rss"/>
            <outline text="E! News" title="E! News" type="rss" xmlUrl="http://uk.eonline.com/syndication/feeds/rssfeeds/topstories.xml"/>
            <outline text="Hollywood Reporter" title="Hollywood Reporter" type="rss" xmlUrl="http://feeds.feedburner.com/thr/news"/>
            <outline text="Reuters Entertainment" title="Reuters Entertainment" type="rss"  xmlUrl="http://feeds.reuters.com/reuters/entertainment"/>
            <outline text="Reuters Music News" title="Reuters Music News" type="rss" xmlUrl="http://feeds.reuters.com/reuters/musicNews"/>
            <outline text="Yahoo Entertainment" title="Yahoo Entertainment" type="rss" xmlUrl="http://rss.news.yahoo.com/rss/entertainment"/>
        </outline>

        <outline title="Sports" text="Sports">
            <outline text="Formula 1" title="Formula 1" type="rss" xmlUrl="http://www.formula1.com/rss/news/latest.rss"/>
            <outline text="MotoGP" title="MotoGP" type="rss" xmlUrl="http://rss.crash.net/crash_motogp.xml"/>
            <outline text="N.Y.Times Track And Field" title="N.Y.Times Track And Field" type="rss" xmlUrl="http://topics.nytimes.com/topics/reference/timestopics/subjects/t/track_and_field/index.html?rss=1"/>
            <outline text="Reuters Sports" title="Reuters Sports" type="rss" xmlUrl="http://feeds.reuters.com/reuters/sportsNews"/>
            <outline text="Yahoo Sports NHL" title="Yahoo Sports NHL" type="rss" xmlUrl="http://sports.yahoo.com/nhl/rss.xml"/>
            <outline text="Yahoo Sports" title="Yahoo Sports" type="rss" xmlUrl="http://rss.news.yahoo.com/rss/sports"/>
        </outline>

        <outline title="Tech" text="Tech">
            <outline text="Coding Horror" title="Coding Horror" type="rss" xmlUrl="http://feeds.feedburner.com/codinghorror/"/>
            <outline text="Gadget Lab" title="Gadget Lab" type="rss" xmlUrl="http://www.wired.com/gadgetlab/feed/"/>
            <outline text="Gizmodo" title="Gizmodo" type="rss" xmlUrl="http://gizmodo.com/index.xml"/>
            <outline text="Reuters Technology" title="Reuters Technology" type="rss" xmlUrl="http://feeds.reuters.com/reuters/technologyNews"/>
        </outline>
    </body>
</opml>"""


TXT2 = """
<opml version="1.0">
    <head>
        <title>rssbot opml</title>
    </head>
    <body>
        <outline title="rssbot opml" text="24/7 feed fetcher">
            <outline name="url1" display_list="title,link,author" xmlUrl="http://hnrss.org/newest"/>
        </outline>
    </body>
</opml>
"""


class TestOPML(unittest.TestCase):

    def test_opml(self):
        res = OPML.parse(TXT, "outline", "title,type,text,xmlUrl")
        self.assertTrue(len(res) == 20)

    def test_import(self):
        res = OPML.parse(TXT2, "outline", "name,display_list,xmlUrl")
        self.assertTrue(len(res) == 1)
