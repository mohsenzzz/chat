from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from user.models import User
from user.serializers import UserRegisterSerializer, UserLoginSerializer, UserUpdateSerializer


class RegisterPhoneNumberAPI(APIView):
    """
    register user: when user insert phone number if phone nimber there is not in
    database , create a new user in database
    """
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        user = User.objects.filter(phone_number=request.data['phone_number']).first()
        if not user:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #snd sms
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer=self.serializer_class(instance=user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLoginAPI(APIView):
    """
    recive phone number and code by user and check if user by this phone number registerd and
    code is true return ok
    """
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = User.objects.filter(phone_number=request.data['phone_number']).first()
        if user:
                if request.data['code'] == '12345':
                    serializer = self.serializer_class(instance=user)
                    token = User.get_token_for_user(user)
                    # print(token)
                    # serializer.data
                    data = serializer.data
                    data['token'] = token
                    print(data)
                    return Response(data, status=status.HTTP_200_OK)
                return Response({'message':'your verify code is in valid!'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'user not found'}, status=status.HTTP_404_NOT_FOUND)


class ProfileUpdateAPI(APIView):
    """
    in this API user can send requests if user login and his/her jwt token is valid:
     1.get user info
     2. update user info (username, phone_number,first_name,last_name,avatar)
     in this API we used from access_token for fetch user form database
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get(self, request):
        user= User.get_user_info_by_token(request.auth)
        serializer = self.serializer_class(instance=user)
        return Response(serializer.data)



    def put(self, request):
        user = User.get_user_info_by_token(request.auth)
        serializer = self.serializer_class(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# class UserAuthenticationAPI(APIView):
#
#     def post(self, request):
#         user = get_object_or_404(User, phone_number=request.data['phone_number'])
#         if not user:
#             User.objects.create(phone_number=request.data['phone_number'])