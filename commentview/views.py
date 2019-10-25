import json
from django.views  import View
from django.http   import JsonResponse
from .models       import Comment

# Create your views here.
class CommentView(View):
    
   def post(self, request):
       comment_data = json.loads(request.body)
       Comment(
               user    = comment_data['user'], 
               comment = comment_data['comment'],
       ).save()

       return JsonResponse({"message" : "SUCCESS" }, status = 200)
               
   def get(self, request):
       comment_list = []
       comments = Comment.objects.all()
       for comment in comments:
           print(comment)
           comment_list.append({
               "id"        : comment.id,
               "user"      : comment.user,
               "comment"   : comment.comment,
               "update"    : comment.updated_at,
               "create"    : comment.created_at,
           })
        
       print(comment_list)
        
       return JsonResponse({"comment_data" : comment_list}, status = 200)

