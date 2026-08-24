
import pytest


# @pytest.mark.api
def test_ui(playwright):
    #basic Auth
    # context = playwright.request.new_context(http_credentials={"username":"us","password":"pw"})
    context = playwright.request.new_context()
    response = context.get("https://dummyjson.com/products/?limit=5", headers={"x-api-key":"api key"})
    print(response)
    responseBody = response.json()
    print(responseBody['products'][0]["title"])

    assert response.status==200

@pytest.mark.api
def test_post(playwright):
    context = playwright.request.new_context()
    requstbody ={
            "title": "put title 11"
            }
    response = context.post("https://dummyjson.com/products/add", headers={"x-api-key":"api key"}, data=requstbody)
    assert response.status==201
    print(response.json())

    