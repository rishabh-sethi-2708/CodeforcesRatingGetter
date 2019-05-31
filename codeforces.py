from urllib.request import urlopen
import json

url = 'https://codeforces.com/api/user.info?handles='
username = input()
final_url=url+username

data = json.load(urlopen(final_url))
#print(data)
new_result = data['result']
for item in new_result:
    rating = item['rating']
    first_name = item['firstName']
    last_name = item['lastName']


print ("Rating of "+first_name +" "+last_name+" is "+str(rating))