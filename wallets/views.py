from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def walletPage(request):
    return render(request, 'pages/wallet/wallet_page.html')