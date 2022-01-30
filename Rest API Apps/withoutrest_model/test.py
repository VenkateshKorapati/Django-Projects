import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
#Single Endpoint Rule 
def get_resource(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
#get_resource(3)

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
# create_resource()

#creating new employee data Using PUT method
def update_resource(id):
    new_emp={
        'id':id,
        'esal':6000,
        'eaddr':'Manali'
    }
    resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
#update_resource(6)

#creating new employee data Using DELETE method
def delete_resource(id):
    data={
    'id':id
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(6)




# def get_resource(id):
#      resp=requests.get(BASE_URL+ENDPOINT+id+'/')
#      print(resp.status_code)
#      print(resp.json())

# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())  

# # creating new employee data Using POST method
# def create_resource():
#     new_emp={
#         'eno':108,
#         'ename':'Nag',
#         'esal':100000,
#         'eaddr':'Bangalore'
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# # create_resource()

# # creating new employee data Using PUT method
# def update_resource(id):
#     new_emp={
#         'esal':6000,
#         'eaddr':'Manali'
#     }
#     resp=requests.put(BASE_URL+ENDPOINT+id+'/',data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# #update_resource('5')

# # creating new employee data Using DELETE method
# def delete_resource(id):
#     resp=requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
#     print(resp.status_code)
#     print(resp.json())
# delete_resource(5)
