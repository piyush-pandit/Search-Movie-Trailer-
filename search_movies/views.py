from django.shortcuts import render, redirect
import requests
from django.conf import settings
import json
import imdb
from rest_framework.response import Response
from django.http import HttpResponse, Http404


def searching_data(request):

    context = {}
    if request.method == "POST" :

        try:
            url = settings.RAPID_API_BASE_URL + \
                f"?s={ request.POST['search'] }&page=1&r=json"
            movie_name = request.POST['search']
            print(request.POST['search'])
            print(url)

            headers = {
                'x-rapidapi-key': settings.IMDB_RAPID_API_KEY,
                'x-rapidapi-host': settings.RAPID_API_HOST_NAME ,
                'useQueryString': 'true',
                'Content-Type': 'application/json'
            }

            payload = json.dumps({
                "upload_date": "",
                "read": "True"
            })


            response = requests.request("GET", url, headers=headers, data=payload)

            print(response.json()['Search'])
            context = {
                    'movie_list': response.json()['Search']
            }
        except Exception as e:
            return render(request, "errorPage.html")

    return render(request, 'find.html', context)


def youtubeTrailer(request,imdb):

    context = {}
    print(type(imdb),imdb)

    url = setting.RAPID_API_BASE_BY_ID

    querystring = {"type":"get-movie-details","imdb":imdb }

    headers = {
        'x-rapidapi-key': settings.IMDB_RAPID_API_KEY,
        'x-rapidapi-host': settings.X_RAPIDAPI_HOST,
        }
    try:

        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.json())
        
        trailerUrl = settings.YT_BASE_URL + response.json()['youtube_trailer_key']
        print(trailerUrl)
        context ={
            'trailerUrl' : trailerUrl,
            'details' : response.json()
        }
    except Exception as e:
        return render(request, "errorPage.html")

    return render(request, 'details.html', context)
