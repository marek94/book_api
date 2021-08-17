# book_api
Django app expose books rest api

Requirements:
- docker
- docker-compose 

Run the app using: docker-compose up

Use the app: get all books - localhost:8000/books fill books with data from https://www.google.com/url?q=https://www.googleapis.com/books/v1/volumes?q=QUERY 

where QUERY is the data passed in the post request: 

POST localhost:8000/db { "q": "Hobbit" } 

It will populate database with books related with Hobbit fetched from extarnal source api
