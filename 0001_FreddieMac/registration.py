import requests
import json 

myheaders = {
   	"x-rapidapi-host": "free-nba.p.rapidapi.com",
	"x-rapidapi-key": "14a8b42a6cmshceb9a36e240a1cep1dc18ejsnf5536497b56e",
	"useQueryString": 'true'
}

x= requests.get('https://free-nba.p.rapidapi.com/stats', headers=myheaders)
t = x.json()
print(t)
