from rest_framework .views import APIView
from rest_framework .response import Response
from .models import lib
class check(APIView):
    def get(self,request):
        if 'id' in request.GET:
            books=lib.objects.filter(id=request.GET['id']).values()
        #Search Panel    
        elif 'bookname' in request.GET:
            books=lib.objects.filter(Book_name__icontains=request.GET['bookname']).values()   
        else:
            books=lib.objects.values()       
        return Response({"NAME":books})


    def post(self,request):
        lib.objects.create(**request.data)
        return Response("Record added")



    def put(self,request):
        id=request.data['id']
        books=request.data
        books.pop('id')
        lib.objects.filter(id=id).update(**books)
        return Response({"message":'record updated'})




  
   