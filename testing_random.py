import http.client, urllib
conn = http.client.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.parse.urlencode({
    "token": "apnths5ztcrmiyac8q6nsyiq37nh2n",
    "user": "gnexfbem3shbhi5g922v68d68i5uqn",
    "message": "",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()