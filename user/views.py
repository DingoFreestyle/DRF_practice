from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import login, authenticate

class UserApiView(APIView):
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(request, username=username, password=password)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


#     class UserView(APIView):
#     permission_classes = [permissions.AllowAny]

#     def GET(self, request):
#         return raise({"message": "GET된다구~"})
#     def POST(self, request):
#         return raise({"message": "POST된다구~"})
#     def PUT(self, request):
#         return raise({"message": "PUT된다구~"})
#     def DELETE(self, request):
#         return raise({"message": "DELETE된다구~"})
#
# def user_view(request):
#     if request.method == "get":
#         pass