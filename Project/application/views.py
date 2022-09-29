from django.shortcuts import render
import json
# import package
import africastalking
from django.views.decorators.csrf import csrf_exempt 
# Create your views here.
@csrf_exempt
def sms(request):
    if request.method =='POST':
        username = "sandbox"    # use 'sandbox' for development in the test environment
        api_key = "cd1b2b77fdf97ee7196fa422561c42b315242e36cc849be769b93c934579377d"      # use your sandbox app API key for development in the test environment
        africastalking.initialize(username, api_key)


        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['phonenumber']
        # Use the service synchronously
        # response = sms.send("Hello Message!", [content])
        # print(response)

        # Or use it asynchronously
        def on_finish(error, response):
            if error is not None:
                raise error
            print(response)

        sms.send("Hello Message!", [content], callback=on_finish)    
