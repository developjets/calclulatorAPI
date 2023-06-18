import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader

def home(request):
    return HttpResponse(render(request, 'calculatorUI/index.html'))

def calculator(request):
    if request.method == 'POST':
        # Retrieve the data from the POST request
        data = request.POST
        # Make the POST request to the external API
        api_url = 'http://127.0.0.1:8000/calculator/api'  # Replace with the actual API URL
        response = requests.post(api_url, data=data)

        # Check if the request was successful (HTTP 200 status code)
        if response.status_code == requests.codes.ok:
            # Retrieve the data from the API response
            api_data = response.json()

            # Process the data as needed

            # Return a JSON response with the processed data
            return JsonResponse(api_data)

    # Return a bad request response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method'}, status=400)