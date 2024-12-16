requirements: 1.postgresql database 2. redis server

apis:

register user:        url: localhost:8000/user/register          data: { "phone_number":"0919....." }

login user:           url: localhost:8000/user/login/            data: { "phone_number":"0919.....", "code":"12345" }

user profile:         url: localhost:8000/user/profile/

chat     url: localhost:8000/user/chat/

users list :        url: localhost:8000/user/list?search=

users chat list:          url: localhost:8000/chat/users?search= 

chat details:     url: localhost:8000/chat/detail/
