
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
@method_decorator(csrf_exempt,name='dispatch')
class EmployeeCRUDCBV(HttpResponseMixin,SerializeMixin,View):
    def get_object_by_id(self,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The Required Resource Not Available with matched id.'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.serialize([emp,])
            return self.render_to_http_response(json_data)

        qs=Employee.objects.all()
        json_data=self.serialize(qs)
        return self.render_to_http_response(json_data)

    #Create Post Method for Single Endpoint Rule
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
    
    #Creating put menthod for Single Endpoint Rule
        
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None: 
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The Required Update performace not possible.'})
                return self.render_to_http_response(json_data,status=404)
        provided_data=json.loads(data)
        original_data={
         'eno':emp.eno,
         'ename':emp.ename,
         'esal':emp.esal,
         'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)

        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource Updated Succesfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    #Creating put menthod for Single Endpoint Rule
        
    def delete(self,request,*args,**kwargs):
        data=request.body
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            emp=self.get_object_by_id(id)
            if emp is None:
                json_data=json.dumps({'msg':'The Matched Resource Not Found and Update performace not possible.'})
                return self.render_to_http_response(json_data,status=404)
        status,delete_object=emp.delete()
        if status==1:
            json_data=json.dumps({'msg':'The required id(data) Operation succesfully deleted'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'The required delete Operation not possible,Id mandatory please provide'})
        return self.render_to_http_response(json_data,status=404)
        


@method_decorator(csrf_exempt,name='dispatch')
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

    def put(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'The Required Update performace not possible.'})
            return self.render_to_http_response(json_data,status=404)
        data=request.body
        valid_json=is_json(data)
        if not valid_json:
            json_data=json.dumps({'msg':'Please send valid json data only'})
            return self.render_to_http_response(json_data,status=400) 

        provided_data=json.loads(data)
        original_data={
         'eno':emp.eno,
         'ename':emp.ename,
         'esal':emp.esal,
         'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)

        form=EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'Resource created Succesfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,id,*args,**kwargs):
        emp=self.get_object_by_id(id)
        if emp is None:
            json_data=json.dumps({'msg':'The Mateched Resource Not Found and Update performace not possible.'})
            return self.render_to_http_response(json_data,status=404)
        status,delete_object=emp.delete()
        if status==1:
            json_data=json.dumps({'msg':'The required id(data) Operation succesfully deleted'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'The required delete Operation not possible'})
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

# # @method_decorator(csrf_exempt,name='dispatch')
# # class EmployeeListCBV(HttpResponseMixin,SerializeMixin,View):
# #     def get(self,request,*args,**kwargs):
# #         qs=Employee.objects.all()
# #         json_data=self.serialize(qs)
# #         return HttpResponse(json_data,content_type='application/json')
# #     def post(self,request,*args,**kwargs):
# #         data=request.body
# #         valid_json=is_json(data)

# #         if not valid_json:
# #             json_data=json.dumps({'msg':'Please send valid json data only'})
# #             return self.render_to_http_response(json_data,status=400)

# #         empdata=json.loads(data)
# #         form=EmployeeForm(empdata)
# #         if form.is_valid():
# #             form.save(commit=True)
# #             json_data=json.dumps({'msg':'Resource created Succesfully'})
# #             return self.render_to_http_response(json_data)
# #         if form.errors:
# #             json_data=json.dumps(form.errors)
# #             return self.render_to_http_response(json_data,status=400)