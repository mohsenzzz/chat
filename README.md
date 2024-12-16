# chat

requirements:
1.postgresql database
2. redis server

urls: 
1. register user:
    url:
       localhost:8000/user/register
   data:
       {
    "phone_number":"0919....."
    }
2. login user:
    url:
       localhost:8000/user/login/
   data:
       {
    "phone_number":"0919.....",
    "code":"12345"
    }
3. user profile:
        url:
           localhost:8000/user/profile/
4. chat
         url:
           localhost:8000/user/chat/<token>

5. users list :
         url:
           localhost:8000/user/list?search=<username or phone_number>
6. users chat list:
          url:
           localhost:8000/chat/users?search=<username or phone_number>
7.chat details:
          url:
           localhost:8000/chat/detail/<chat-token>           
