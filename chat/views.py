from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from chat.models import Message
from django.db.models import Count
from django.shortcuts import redirect
from chat.serializers import Messageserializer
from django.views.decorators.http import require_http_methods
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
@require_http_methods(["GET", "POST"])
def notification_list(request):
    """
    List all messages from the authenticated user
    """
    from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
    if request.method == 'GET':
        page_nr = request.GET.get('page_nr',1)
        page_limit = request.GET.get('page_limit',10)
        try:
            # check if the user is authenticated otherwise redirect to login page
            if request.user.is_authenticated:
                messages = Message.objects.filter(receiver=request.user).order_by('-created_on')#.values("sender").annotate(count=Count("receiver"))
                paginator = Paginator(messages, page_limit)
                page = paginator.page(page_nr)
                serializer = Messageserializer(page, many=True)
                return JSONResponse(serializer.data)
            else:
                return redirect('/admin/login/?next=/messages/')
        except EmptyPage:
            return JSONResponse([], status=200)
        except PageNotAnInteger:
            return JSONResponse({'error': 'invalid page_nr or page_limit'}, status=400)
    if request.method == 'POST':
        if request.user.is_authenticated:
            data = JSONParser().parse(request)
            serializer = Messageserializer(data=data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=201)
            else:
                return JSONResponse(serializer.errors, status=400)
        else:
            return redirect('/admin/login/?next=/messages/')

@csrf_exempt
@require_http_methods(["GET", "DELETE"])
def notification_details(request,message_id):
    if request.user.is_authenticated:
        try:
            message = Message.objects.get(id=message_id)
        except Message.DoesNotExist:
            return JSONResponse({'error': 'message not found'}, status=404)
        if request.method == 'GET':
            serializer = Messageserializer(message, many=False)
            return JSONResponse(serializer.data, status=200)
        if request.method == 'DELETE':
            message.delete()
            return HttpResponse(status=204)
    else:
        return redirect('/admin/login/?next=/messages/{}/'.format(message_id))



