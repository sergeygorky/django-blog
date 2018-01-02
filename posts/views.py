from django.http import HttpResponse
from django.shortcuts import render


def post_home():
    return HttpResponse("<h1>Hello!</h1>")
