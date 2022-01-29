
from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
#from django.core.serializers import serialize
from testapp.mixins import SerializeMixin,HttpResponseMixin

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm

# Create your views here.
class EmployeeDetailsCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data=json.dumps({'msg':'The Required Data Not Available'})
            return self.render_to_http_response(json_data,status=404)
        else:
            json_data=self.serialize([emp,])
            
            return self.render_to_http_response(json_data)
        #emp=Employee.objects.get(id=id)
        # emp_data={
        #     'eno':emp.eno,
        #     'ename':emp.ename,
        #     'esal':emp.esal,
        #     'eaddr':emp.eaddr,
        #     }
        # json_data=json.dumps(emp_data)
        # return HttpResponse(json_data,content_type='application/json')

# class EmployeeListCBV(View):
#     def get(self,request,*args,**kwargs):
#         qs=Employee.objects.all()
#         json_data=serialize('json',qs)
#         p_data=json.loads(json_data)
#         final_list=[]
#         for obj in p_data:
#             emp_data=obj['fields']
#             final_list.append(emp_data)
#         json_data=json.dumps(final_list)
#         return HttpResponse(json_data,content_type='application/json')

@method_decorator(csrf_exempt,name='dispatch')
class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)

        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)

        empdata=json.loads(data)
        form=EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created Succesfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)