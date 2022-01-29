import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resource(id):
     resp=requests.get(BASE_URL+ENDPOINT+id+'/')
     print(resp.status_code)
     print(resp.json())

def get_all():
    resp=requests.get(BASE_URL+ENDPOINT)
    print(resp.status_code)
    print(resp.json())  

# creating new employee data Using POST method
def create_resource():
    new_emp={
        'eno':108,
        'ename':'Nag',
        'esal':100000,
        'eaddr':'Bangalore'
    }
    resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
create_resource()