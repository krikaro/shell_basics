#!/usr/bin/python3
import requests

def get_youtube_url(recipe_name):
    recipe = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?s={}'.format(recipe_name))
    if recipe.status_code != 200:
        return
    if recipe.json() and 'meals' in recipe.json().keys():
        if recipe.json()['meals'] and len(recipe.json()['meals']) > 0:
            url = recipe.json()['meals'][0]['strYoutube']
            print(url)

recipes = ['paella', 'lassagna', 'penne']
for recipe in recipes:
    get_youtube_url(recipe)
