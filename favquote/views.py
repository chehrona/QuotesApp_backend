from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quote
from .serializers import QuoteSerializer



@api_view(['GET'])
def get_quotes(request):
    quotes = Quote.objects.all()[(Quote.objects.count() - 4):]
    print(quotes)
    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def send_quote(request):
    print(request)
    serializer = QuoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    quotes = Quote.objects.all()[(Quote.objects.count() - 4):]
    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data)

