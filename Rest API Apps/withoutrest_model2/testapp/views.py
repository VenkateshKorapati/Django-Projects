from django.shortcuts import render
from django.views.generic import View
import json
from testapp.utils import is_json
from testapp.models import Student
from testapp.mixins import SerializeMixin,HttpResponseMixin
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import StudentForm
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentCRUDcbv(SerializeMixin,HttpResponseMixin,View):
    def get_object_id(self,id):
        try:
            student=Student.objects.get(id=id)
        except Student.DoesNotExist:
            student=None
        return student
    def get(self,request,*args,**kwargs):
        data=request.body
        valid_data=is_json(data)
        if not valid_data:
            json_data=json.dumps({'msg':'The provided data is not Json data'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            student=self.get_object_id(id)
            if student is None:
                json_data=json.dumps({'msg':'The matched ID is not available...provide valid id'})
                return self.render_to_http_response(json_data,status=404)
            json_data=self.serailize([student,])
            return self.render_to_http_response(json_data)
        qs=Student.objects.all()
        json_data=self.serailize(qs)
        return self.render_to_http_response(json_data)

    #Creating Post method
    def post(self,request,*args,**kwargs):
        data=request.body
        valid_data=is_json(data)
        if not valid_data:
            json_data=json.dumps({'msg':'The provided data is not Json data'})
            return self.render_to_http_response(json_data,status=400)
        studentdata=json.loads(data)
        form=StudentForm(studentdata)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'The Student data created Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)
    #create Put Method
    def put(self,request,*args,**kwargs):
        data=request.body
        valid_data=is_json(data)
        if not valid_data:
            json_data=json.dumps({'msg':'The provided data is not Json data'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            student=self.get_object_id(id)
            if student is None:
                json_data=json.dumps({'msg':'The matched ID is not available...provide valid id'})
                return self.render_to_http_response(json_data,status=404)
            
        provided_data=json.loads(data)
        original_data={
        'name':student.name,
        'rollno':student.rollno,
         'marks':student.marks,
        'branch':student.branch,
        }
        original_data.update(provided_data)
        form=StudentForm(original_data,instance=student)
        if form.is_valid():
            form.save(commit=True)
            json_data=json.dumps({'msg':'The Student data created Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data=json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data=request.body
        valid_data=is_json(data)
        if not valid_data:
            json_data=json.dumps({'msg':'The provided data is not Json data'})
            return self.render_to_http_response(json_data,status=400)
        p_data=json.loads(data)
        id=p_data.get('id',None)
        if id is not None:
            student=self.get_object_id(id)
            if student is None:
                json_data=json.dumps({'msg':'The matched ID is not available...provide valid id'})
                return self.render_to_http_response(json_data,status=404)
        status,delete_object=student.delete()
        if status==1:
            json_data=json.dumps({'msg':'The required id(data) Operation succesfully deleted'})
            return self.render_to_http_response(json_data)
        json_data=json.dumps({'msg':'The required delete Operation not possible,Id mandatory please provide'})
        return self.render_to_http_response(json_data,status=404)