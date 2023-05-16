@regression
Feature: Verify the information for all the albums.

    This feature validates that all the albums contain the expected information, 

    Scenario: Get all albums and validate the information

        Given This api "jsonplaceholder.typicode.com/albums"
        When I do a "GET" request
        Then the json response should be equal to json expected "all albums"
