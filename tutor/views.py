from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .util import otp_generator, send_otp_email, validate_otp
from .models import User,Class,Connect,Connect_Message,Connect_Message_Attach
from .serializers import UserSerializer,ClassSerializer,ConnectSerializer,CnctMsgSerializer,CMAttachSerializer
from django import template
# Create your views here.


# HomePage
def home(request):
    return render( request , 'home.html')

# LoginPage
def login(request):
    return render( request , 'login.html')

# SignupPage
def signup(request):
    return render( request , 'signup.html')

def proOne(request,pk=None):
    user_id = pk
    return render( request , 'pro1.html', {'usr_id': user_id})

def proTwo(request,pk=None):
    user_id = pk
    return render( request , 'pro2.html', {'usr_id': user_id})

def search(request):
    return render( request , 'search.html')

def chat(request):
    return render( request , 'messages.html')

def myclasses(request):
    return render( request , 'myclasses.html')

def notification(request):
    return render( request , 'notification.html')

def messages(request):
    return render( request , 'messages.html')

def contactSupport(request):
    return render( request , 'contactSupport.html')

def sndRegister(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    pwd = request.GET.get('pwd')
    usertype = request.GET.get('type')
    otp = request.GET.get('otp')

    sent_otp = request.session['auth_otp']
    sent_email = request.session['auth_email']
    
    result = validate_otp(otp, sent_otp, email, sent_email)

    if not result["success"]:
        return redirect('register')

    result = {"success": True, "message": "User Registered"}
    userentryqry = User.objects.create(username=username, email_id=email, password=pwd, role_id=usertype)
    #if user exist - go to search page
    if  userentryqry  :
        request.session['userid'] = userentryqry.id
        return render( request , 'VI/Profilepage-01/index.html')
    else:
        return redirect('register')


def sendOtp(request):
    return render(request, 'otp.html')

def send_otp(request):
    email = request.GET.get('email')

    validation = validate_email(email)
    if not validation:
        otp = otp_generator()
        otp_status = send_otp_email(email, otp)
        if not otp_status:
            result = {"success": False, "message": "incorrect email"}
            return render( request , 'otp.html')

        request.session["auth_otp"] = otp
        request.session["auth_email"] = email
    
        result = {"successs": True, "message": "otp sent"}
        return render( request , 'VI/Registration-Page/index.html')
    else:
        return redirect('sendOtp')

def validate_email(new_email):
    validateuser = User.objects.raw("select * from user where email_id = '"+ new_email + "';")
    if  validateuser  :
        for i in validateuser : 
            return True
    else:
        return False
    
# User Table
@api_view(['GET','POST','PUT','DELETE'])
def user_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            usr = User.objects.get(user_id=id)
            serializer= UserSerializer(usr)
            return Response(serializer.data)
        usr= User.objects.all()
        serializer=UserSerializer(usr,many=True)
        return Response(serializer.data) 

    if request.method== 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = pk
        usr = User.objects.get(user_id=id)
        serializer= UserSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method== 'DELETE':
        id = pk
        usr= User.objects.get(user_id=id)
        usr.delete()
        return Response({'msg':'Data deleted'})

@api_view(['GET','POST','PUT'])
def task(request):
    if request.method == 'GET':
        usr = User.objects.all()
        serializer = UserSerializer(usr,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('user_id')
        usr = User.objects.get(user_id=id)
        serializer= UserSerializer(usr,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Class table

@api_view(['GET','DELETE'])
def class_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            Clss = Class.objects.get(class_id=id)
            serializer= ClassSerializer(Clss)
            return Response(serializer.data)

    if request.method== 'DELETE':
        id = pk
        clss= Class.objects.get(class_id=id)
        #serializer = ClassSerializer(clss)
        #return Response(serializer.data)
        clss.delete()
        return Response(serializer.data)

    

@api_view(['GET','POST','PUT'])
def class_task(request):
    if request.method == 'GET':
        clss = Class.objects.all()
        serializer = ClassSerializer(clss,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('class_id')
        clss = Class.objects.get(class_id=id)
        serializer= ClassSerializer(clss,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#Connect table

@api_view(['GET','DELETE'])
def connect_api(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cnct = Connect.objects.get(connect_id=id)
            serializer= ConnectSerializer(cnct)
            return Response(serializer.data)

    if request.method== 'DELETE':
        id = pk
        cnct= Connect.objects.get(connect_id=id)
        #serializer = ConnectSerializer(cnct)
        #return Response(serializer.data)
        cnct.delete()
        return Response({'msg':'Data deleted'})

    

@api_view(['GET','POST','PUT'])
def connect_task(request):
    if request.method == 'GET':
        cnct = Connect.objects.all()
        serializer = ConnectSerializer(cnct,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=ConnectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('connect_id')
        cnct = Connect.objects.get(connect_id=id)
        serializer= ConnectSerializer(cnct,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#Connect_Massage Table
@api_view(['GET','DELETE'])
def connect_msgapi(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cnctmsg = Connect_Message.objects.get(connect_message_id=id)
            serializer= CnctMsgSerializer(cnctmsg)
            return Response(serializer.data)

    if request.method== 'DELETE':
        id = pk
        cnctmsg= Connect_Message.objects.get(connect_message_id=id)
        #serializer = CnctMsgSerializer(cnctmsg)
        #return Response(serializer.data)
        cnctmsg.delete()
        return Response({'msg':'Data deleted'})

    

@api_view(['GET','POST','PUT'])
def connect_msgtask(request):
    if request.method == 'GET':
        cnctmsg = Connect_Message.objects.all()
        serializer = CnctMsgSerializer(cnctmsg,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=CnctMsgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('connect_message_id')
        cnctmsg = Connect_Message.objects.get(connect_message_id=id)
        serializer= CnctMsgSerializer(cnctmsg,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# Connect_message_attach

@api_view(['GET','DELETE'])
def connect_msg_Attachapi(request,pk=None):
    if request.method =='GET':
        id = pk
        if id is not None:
            cma = Connect_Message_Attach.objects.get(id=id)
            serializer= CMAttachSerializer(cma)
            return Response(serializer.data)

    if request.method=='DELETE':
        id = pk
        cma= Connect_Message_Attach.objects.get(id=id)
        #serializer = CMAttachSerializer(cma)
        #return Response(serializer.data)
        cma.delete()
        return Response({'msg':'Data deleted'})

    

@api_view(['GET','POST','PUT'])
def connect_msg_attachtask(request):
    if request.method == 'GET':
        cma = Connect_Message_Attach.objects.all()
        serializer = CMAttachSerializer(cma,many=True)
        return Response(serializer.data)

    if request.method== 'POST':
        serializer=CMAttachSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Create'})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id = request.data.get('connect_message_id')
        cma = Connect_Message_Attach.objects.get(connect_message_id=id)
        serializer= CMAttachSerializer(cma,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)