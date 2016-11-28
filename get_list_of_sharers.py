from facepy import *

access_token = "*INSERT FACEBOOK ACCESS TOKEN HERE*"
graph = GraphAPI(access_token)

g = graph.get('POST-ID_FACEBOOK-ID-NUMERICAL/sharedposts')

for share in g['data']:
    print(share['from']['name'] + " - " + str(share['from']['id']))