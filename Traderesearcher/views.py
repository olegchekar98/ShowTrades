from django.shortcuts import render
import calendar
import krakenex


# Create your views here.
def start(request):
    return render(request, 'Traderesearcher/trade.html', {})

def show_trade(request):
    kraken = krakenex.API()

    response = kraken.query_public('Trades', {'pair': 'XXBTZUSD'})
    print(response)
    return render(request, 'Traderesearcher/trade.html', {'response': response})
