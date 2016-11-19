from login.models import User
from login.serializers import SnippetSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


login_url = 'login/login.html'
logedin_url = 'login/logged_in.html'
signup_url = 'login/signup.html'


@api_view(['GET', 'POST'])
def snippet_login(request):

    """
    User Login Page
    """

    if request.method == 'GET':
        return Response(template_name=login_url)

    if request.method == 'POST':
        uname = request.data.get('username')
        psw = request.data.get('password')
        try:
            users = User.objects.get(username=uname, password=psw)
            return Response(template_name=logedin_url)
        except User.DoesNotExist:
            error_message = "Please Enter Correct username and password"
            return Response({'error_message': error_message}, template_name=login_url)


@api_view(['GET', 'POST'])
def snippet_signup(request):

    """
    Users Sign Up Page
    """
    if request.method == 'GET':
        return Response(template_name=signup_url)

    if request.method == 'POST':
        try:
            uname = request.data.get('username')
            users = User.objects.get(username=uname)
            error_message = "User Name Already Exist"
            return Response({'error_message': error_message}, template_name=signup_url)
        except User.DoesNotExist:
            usercreate = SnippetSerializer(data=request.data)
            if usercreate.is_valid():
                usercreate.save()
                return Response(template_name=logedin_url)
            else:
                return Response(template_name=signup_url)
