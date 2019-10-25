import jwt
import json
import bcrypt
from django.views  import View
from django.http   import JsonResponse
from .models       import User
# Create your views here.

class SignUp(View):   
    
    def post(self, request):
        user_data = json.loads(request.body)
        pw_byte   = bytes(user_data['password'], encoding='utf-8')
        print(pw_byte)
        encrypted_pw = bcrypt.hashpw(pw_byte, bcrypt.gensalt())
        print(encrypted_pw)
        print(type(encrypted_pw))
        decrypted_pw = encrypted_pw.decode('utf-8')
        print(decrypted_pw)
        print(type(decrypted_pw))

        User(
             username         = user_data['username'], 
             password         = decrypted_pw,
             email            = user_data['email'],
        ).save()
        
        return JsonResponse({"message":"SUCCESS"}, status=200)

class AuthView(View):
    def post(self, request):
        auth_data = json.loads(request.body)
        print(auth_data)
        jwt_algo = 'HS256'
        
        try:
            user = User.objects.get(email=auth_data['email'])
            print(user)
            
            if bcrypt.checkpw(auth_data['password'].encode('utf-8'), user.password.encode('utf-8')):

                token = jwt.encode({'user' : user.password}, 'secret_key', jwt_algo)
                result = {"message" : "SUCCESS SIGNIN"} 
                return JsonResponse(result, status=200)
            else:
                return JsonResponse({"message": "INVALID_PASSWORD"}, status=401)
        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=401)
  

