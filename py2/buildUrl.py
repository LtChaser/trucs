import re


#crid://2F//2Fbds.tv//2F273719482-imi:0010000000D1D875

crid = 'crid://2F//2Fbds.tv//2F273719482-imi:0010000000D1D875'
webcrid = re.sub('/', '~', crid)
print webcrid

url = 'https://web-api-pepper.horizon.tv/oesp/v2/NL/nld/web/listings/' + webcrid
print url

