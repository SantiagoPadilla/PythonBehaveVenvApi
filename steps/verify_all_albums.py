from behave import given, when, then
import logging as log
import requests
import json
from common_configs import apisConfig

@then('The "{navBar}" bar should be visible')
def verify_nav_bars_visible(context, navBar):
    pass

@given('This api "{api}"')
def step_impl(context, api):
    context.requested_api = apisConfig.APICONFIG.get(api)
    pass

@when('I do a "{verb}" request')
def step_impl(context, verb):
    context.requested_verb = verb
    
    response = requests.get(context.requested_api)
    context.res_json = response.json()
    assert response.status_code == 200
    pass

@then('the json response should be equal to json expected "all albums"')
def step_impl(context):
    
    with open("json_data\\all_albums.json", 'r') as file:
        json_file = json.load(file)
    
    assert json_file == context.res_json
    pass

@when('I do a "{verb}" request with client credentials')
def step_impl(context, verb):
    context.requested_verb = verb

    token_url = "https:token"
    data = {
        "grant_type": "client_credentials",
        "client_id": "tu_client_id",
        "client_secret": "tu_client_secret"
    }

    response = requests.post(token_url, data=data)
    assert response.status_code == 200

    access_token = response.json().get("access_token")

    headers = {"Authorization": "Bearer {access_token}"}
    response = requests.get(context.requested_api, headers=headers)
    context.res_json = response.json()
    assert response.status_code == 200
    
@when('I do a "{verb}" request with authorization code')
def step_impl(context, verb):
    context.requested_verb = verb

    authorization_code = "authorization"

    token_url = "token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "client_id": "tu_client_id",
        "client_secret": "tu_client_secret",
        "redirect_uri": "tu_redirect_uri"
    }

    response = requests.post(token_url, data=data)
    assert response.status_code == 200

    access_token = response.json().get("access_token")

    headers = {"Authorization": "Bearer {access_token}"}
    response = requests.get(context.requested_api, headers=headers)
    context.res_json = response.json()
    assert response.status_code == 200