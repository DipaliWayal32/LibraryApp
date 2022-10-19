from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Library.models import Library
from Library.serializers import LibrarySerializer

from django.core.files.storage import default_storage

# Create your views here.


def LibraryApi(request,id=0):
    if request.method=='GET':
        Library =  Library.objects.all()
        Library_serializer= LibrarySerializer( Library,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    elif request.method=='POST':
        Library_data=JSONParser().parse(request)
        employees_serializer= LibrarySerializer(data=Library_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        Library_data=JSONParser().parse(request)
        Library= Library.objects.get(LibraryId=Library_data[' LibraryId'])
        Library_serializer= LibrarySerializer(Library,data=Library_data)
        if Library_serializer.is_valid():
           Library_serializer.save()
        return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        Library= Library.objects.get( LibraryId=id)
        Library.delete()
        return JsonResponse("Deleted Successfully",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)