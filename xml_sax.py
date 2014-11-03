#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.parsers.expat import ParserCreate
db = []

class DefaultSaxHandler(object):
	def start_element(self, name, attrs):
		#print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))
		if name == 'yweather:forecast':
			db2 = {}
			db2['code']= attrs['code']
			db2['text']= attrs['text']
			db2['high']= attrs['high']
			db2['low']= attrs['low']
			db2['date']= attrs['date']
			db2['day']= attrs['day']
			db.append(db2)
	def end_element(self, text):
		#print('sax:end_element: %s' % text)
		pass

	def char_data(self, text):
		#print('sax:char_data: %s' % text)
		pass

def Parsedb(db):
	print db(0)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''

xml_weather = r'''<rss xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#" version="2.0">
<channel>
<title>Yahoo! Weather - Beijing, CN</title>
<link>
http://u.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html
</link>
<description>Yahoo! Weather for Beijing, CN</description>
<language>en-us</language>
<lastBuildDate>Sun, 26 Oct 2014 8:01 am CST</lastBuildDate>
<ttl>60</ttl>
<yweather:location city="Beijing" region="" country="China"/>
<yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
<yweather:wind chill="14" direction="40" speed="25.75"/>
<yweather:atmosphere humidity="30" visibility="9" pressure="1024.1" rising="0"/>
<yweather:astronomy sunrise="6:35 am" sunset="5:20 pm"/>
<image>
<title>Yahoo! Weather</title>
<width>142</width>
<height>18</height>
<link>http://weather.yahoo.com</link>
<url>
http://l.yimg.com/a/i/brand/purplelogo//uh/us/news-wea.gif
</url>
</image>
<item>
<title>Conditions for Beijing, CN at 8:01 am CST</title>
<geo:lat>39.91</geo:lat>
<geo:long>116.39</geo:long>
<link>
http://us.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html
</link>
<pubDate>Sun, 26 Oct 2014 8:01 am CST</pubDate>
<yweather:condition text="Partly Cloudy" code="30" temp="14" date="Sun, 26 Oct 2014 8:01 am CST"/>
<description>
<![CDATA[
<img src="http://l.yimg.com/a/i/us/we/52/30.gif"/><br /> <b>Current Conditions:</b><br /> Partly Cloudy, 14 C<BR /> <BR /><b>Forecast:</b><BR /> Sun - Sunny. High: 16 Low: 4<br /> Mon - Sunny. High: 13 Low: 2<br /> Tue - Mostly Sunny. High: 14 Low: 4<br /> Wed - Partly Cloudy. High: 17 Low: 8<br /> Thu - Partly Cloudy. High: 18 Low: 9<br /> <br /> <a href="http://us.rd.yahoo.com/dailynews/rss/weather/Beijing__CN/*http://weather.yahoo.com/forecast/CHXX0008_c.html">Full Forecast at Yahoo! Weather</a><BR/><BR/> (provided by <a href="http://www.weather.com" >The Weather Channel</a>)<br/>
]]>
</description>
<yweather:forecast day="Sun" date="26 Oct 2014" low="4" high="16" text="Sunny" code="32"/>
<yweather:forecast day="Mon" date="27 Oct 2014" low="2" high="13" text="Sunny" code="32"/>
<yweather:forecast day="Tue" date="28 Oct 2014" low="4" high="14" text="Mostly Sunny" code="34"/>
<yweather:forecast day="Wed" date="29 Oct 2014" low="8" high="17" text="Partly Cloudy" code="30"/>
<yweather:forecast day="Thu" date="30 Oct 2014" low="9" high="18" text="Partly Cloudy" code="30"/>
<guid isPermaLink="false">CHXX0008_2014_10_30_7_00_CST</guid>
</item>
</channel>
</rss>
<!--
 fe468.global.media.gq1.yahoo.com Sat Oct 25 18:06:50 PDT 2014 
-->
'''

handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml_weather)
print db[0]
#Parsedb(db)

#if __name__=='__main__':


