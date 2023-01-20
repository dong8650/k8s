import requests
import json

ZABBIX_API_URL = "http://zabbix.tossdata.bz/api_jsonrpc.php"
UNAME = "Admin"
PWORD = "zabbix"

r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "user.login",
                      "params": {
                          "user": UNAME,
                          "password": PWORD},
                      "id": 1
                  })

#print(json.dumps(r.json(), indent=4, sort_keys=True))

'''
  r.json => print => {'jsonrpc': '2.0', 'result': 'fcb4494276277264c10da160e3de5731', 'id': 1}
resp = r.json()
  resp => print => {'jsonrpc': '2.0', 'result': 'fcb4494276277264c10da160e3de5731', 'id': 1}
sessionid = resp["result"]
  sessionid => print => fcb4494276277264c10da160e3de5731


  r.json => print => {'jsonrpc': '2.0', 'result': 'fcb4494276277264c10da160e3de5731', 'id': 1}
sessionid = r.json()["result"]
  sessionid => print => fcb4494276277264c10da160e3de5731
'''

AUTHTOKEN = r.json()["result"]

print(AUTHTOKEN)

'''
# Retrieve a list of problems
print("\nRetrieve a list of problems")
r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "problem.get",
                      "params": {
                          "output": "extend", 
                          "selectAcknowledges": "extend", 
                          "recent": "true", 
                          "sortfield": ["eventid"],
                          "sortorder": "DESC"
                      },
                      "id": 2,
                      "auth": AUTHTOKEN
                  })

print(json.dumps(r.json(), indent=4, sort_keys=True))
'''


r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "hostgroup.get",
                      "params": {
                          "output": "extend", 
                          "filter": {
                            "name": [
                            "Linux servers"
                            ]
                          }
                      },
                      "id": 1,
                      "auth": AUTHTOKEN
                  })

print(json.dumps(r.json(), indent=4, sort_keys=True))

GROUPID = r.json()["result"][0]['groupid']

r = requests.post(ZABBIX_API_URL,
                  json={
                      "jsonrpc": "2.0",
                      "method": "host.get",
                      "params": {
                            "output": ["name"],
                            "groupids": GROUPID
                      },
                      "id": 1,
                      "auth": AUTHTOKEN
                  })

print(json.dumps(r.json(), indent=4, sort_keys=True))

HOSTS = r.json()["result"]

print(HOSTS)

for x in range(len(HOSTS)): 
    print(HOSTS[x]['name'])


