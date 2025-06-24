import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import requests
from wallets.models import Wallet
from django.contrib import messages

@login_required(login_url='/login')
def walletPage(request):
    wallet = Wallet.objects.get(user = request.user)
    return render(request, 'pages/wallet/wallet_page.html', {'wallet':wallet})


@csrf_exempt
def verify_payment(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        token = data.get('token')
        amount = data.get('amount')

        # Verify the payment with Khalti's API
        url = "https://khalti.com/api/v2/payment/verify/"
        headers = {
            "Authorization": "test_public_key_9ecd180c7edb4c72a4348a15ed175a75",  # Replace with your Khalti secret key
            "Content-Type": "application/json"
        }
        payload = {
            "token": token,
            "amount": amount
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response_data = response.json()

            # Debugging output to see what Khalti returns
            print("Response from Khalti:", response_data)

            # Check if the response status code is 200
            # if response.status_code == 200 and response_data.get("idx"):
            wallet = Wallet.objects.get(user = request.user)
            wallet.balance = wallet.balance+amount
            wallet.save()
            messages.success(request, "Fund Added successfully!")
            return redirect('/wallet')
            # else:
            #     return JsonResponse({
            #         'status': 'Payment Failed',
            #         'error': response_data.get('message', 'Unknown error')
            #     }, status=400)

        except Exception as e:
            print("Error during payment verification:", str(e))
            return JsonResponse({'status': 'Payment Failed', 'error': str(e)}, status=400)

    return JsonResponse({'status': 'Invalid Request'}, status=400)

def khalti_payment(request):
    if request.method == "POST":
        product_identity = request.POST.get("product_identity")
        amount = request.POST.get("amount")
        return JsonResponse({
            "success": True,
            "product_identity": product_identity,
            "amount": amount,
            "message": "Redirect to Khalti"
        })
    return render(request, 'paywithkhalti.html')