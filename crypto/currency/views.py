from django.shortcuts import render

# Create your views here.
def home(request):
    #API request handle
    import requests
    import json
    #crypto price data
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price=price_request.json()
    ##Crypto  NEws
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=api_request.json()
    
    return render(request,'home.html',{'api': api, 'price':price })


def prices(request):
    if request.method=="POST":
        import requests
        import json
        #crypto price data
        quote=request.POST['quote']
        quote=quote.upper()
        crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=USD")
        crypto=crypto_request.json()
        return render(request,'prices.html',{'quote':quote,'crypto': crypto})
    else:
        notfound="enter a crypto currency value"
        return render(request,'prices.html',{'notfound':notfound})