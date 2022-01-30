import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='jsoncbv/'
resonse= requests.get(BASE_URL+ENDPOINT)
data=resonse.json()
print(data)
  # print('#'*50)
  #   print('Employee no:',data['eno'])
  #  print('Employee name:',data['ename'])
  #  print('Employee salary:',data['esal'])
  #  print('Employee address:',data['eaddr'])