@regression
Feature: Verify the information for all the albums.

    This feature validates that all the albums contain the expected information, 

    Scenario: Get all albums and validate the information, request with client credentials

        Given This api "albums"
        When I do a "GET" request with client credentials
        Then the json response should be equal to json expected "all albums"
    
    Scenario: Get all albums and validate the information, request with authorization code

        Given This api "albums"
        When I do a "GET" request with authorization code
        Then the json response should be equal to json expected "all albums"