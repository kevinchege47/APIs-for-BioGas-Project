from django.shortcuts import render
import json
import http.client
import json
from django.http import HttpResponse
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

        sms.send("Hello Expert, A Farmer Requested for your Services, Kindly contact them for further Details.Their phone Number is, +254701020901.", [content], callback=on_finish)    
@csrf_exempt
def stanbic(request):
    if request.method =='POST': 
        conn = http.client.HTTPSConnection("api.connect.stanbicbank.co.ke")
        payload = '''{
        "originatorAccount": {
            "identification": {
            "mobileNumber": "254759459364"
            }
        },
        "requestedExecutionDate": "2022-12-01",
        "dbsReferenceId": "21899424091968",
        "txnNarrative": "TRANSACTION NARRATIVE",
        "callBackUrl": "http://client_domain.com/omnichannel/esbCallback",
        "transferTransactionInformation": {
            "instructedAmount": {
            "amount": "10.00",
            "currencyCode": "KES"
            },
            "mobileMoneyMno": {
            "name": "MPESA"
            },
            "counterparty": {
            "name": "J. Sparrow",
            "mobileNumber": "254797292290",
            "postalAddress": {
                "addressLine1": "Some street",
                "addressLine2": "99",
                "postCode": "1100 ZZ",
                "town": "Amsterdam",
                "country": "NL"
            }
            },
            "remittanceInformation": {
            "type": "UNSTRUCTURED",
            "content": "SALARY"
            },
            "endToEndIdentification": "5e1a3da132cc"
        }
        }'''

        headers = {
            'Authorization': "Bearer AAIgMTc0YTQxNGFmZWVlNjA4NWUzODNhYmZkNjgxNjFmNzG79HRQdzaMdS9pB1ZaleCkU-OTvt3Mnp4fjWj2fcQwP7ixj7ZnYSHaWXTRiqz40_mJ3CkHmBft1cfkO3TL1WvikhGfr3dScdHs_CfQayfEUun4xrU_FAzbE_-lLJ3zGnY",
            'content-type': "application/json",
            'accept': "application/json"
            }

        conn.request("POST", "/api/sandbox/mobile-payments/", payload, headers)

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))
        m_pay = json.loads(data)
        pay = json.dumps(m_pay,indent=4,sort_keys=True)
        # print(type(pay))
        print(pay)
        return HttpResponse(pay)
        
        
