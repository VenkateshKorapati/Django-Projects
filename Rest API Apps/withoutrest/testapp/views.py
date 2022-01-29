from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Delhi'
    }
    response='<h1>Employee number:{}<br>Employee name:{}<br>Employee salary:{}<br>Employee address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(response)
import json
def emp_data_jsonview(request):
    emp_data={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Delhi'
        }
    json_data=json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Delhi'
        }
    
    return JsonResponse(emp_data)

from django.views.generic import View
class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data={
        'eno':100,
        'ename':'Sunny',
        'esal':10000,
        'eaddr':'Delhi'
        }
        return JsonResponse(emp_data)


from django.views.generic import View
from testapp.mixins import HttpResponseMixin
class JsonCBV(HttpResponseMixin,View):

    def get(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This message from GET Method'})
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This message from POST Method'})
        return self.render_to_http_response(json_data)

    def put(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This message from PUT Method'})
        return self.render_to_http_response(json_data)

    def delete(self,request,*args,**kwargs):
        json_data=json.dumps({'msg':'This message from DELETE Method'})
        return self.render_to_http_response(json_data)


