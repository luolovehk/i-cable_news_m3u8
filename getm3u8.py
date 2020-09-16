#!/usr/bin/python3
url = 'https://m-epg.cmishow.com:1443/?s=104&p=mLiveChannel&k=1&v=1&c=1&a=852&i=3&channelId=1568275619470108006&l=zh_TW'
import requests
import json
import re
response = requests.get(url)
data = json.loads(response.text)
m3u8 = data['data']['detail']['livePlayurls'][0]['playurl']
m3u8 = re.sub(".m3u8",r'-3.m3u8', m3u8)
f = open("icable.m3u8", 'w')
f.write("#EXTM3U"+'\n')
f.write("#EXT-X-VERSION:6"+"\n")
f.write("#EXT-X-INDEPENDENT-SEGMENTS"+"\n")
f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1"+"\n")
f.write(m3u8)
f.close()
print(m3u8)