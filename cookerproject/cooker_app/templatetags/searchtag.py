from django import template
from django.shortcuts import render, get_object_or_404, redirect
from cooker_app.models import Article
from cooker_app.forms import SearchForm
from django.contrib.postgres.search import SearchVector, SearchRank, SearchQuery
from django.http import HttpResponseRedirect

register = template.Library()
@register.inclusion_tag('search_menu.html')

def search_menu():
   pass
