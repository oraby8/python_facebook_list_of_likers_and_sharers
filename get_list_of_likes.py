import requests
import json

post_id = "*INSERT FACEBOOK POST ID HERE*"
access_token = "*INSERT FACEBOOK ACCESS TOKEN HERE*"
template = "https://graph.facebook.com/v2.4/%s?fields=likes&access_token=%s"
url = template % (post_id, access_token,)
likes = []
first = True
while 1:
	r = requests.get(url)
	result = r.json()
	print(result)
	if first:
		page_likes = result['likes']
		first = False
	else:
		page_likes = result
	likes += page_likes['data']
	if ('next' not in page_likes['paging']):
		break
	url = page_likes['paging']['next']

fp = open("%s_likes.csv" % (post_id), "w")

for liker in likes:
	fp.write(liker['name'] + " - " + "https://facebook.com/" + liker['id'] + "\n")
fp.close()