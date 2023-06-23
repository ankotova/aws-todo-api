Hello, my name is Anastasiia 
lambda_function.py is the code currently running on AWS Lambda. To test the functionality you can run examples from below on the terminal

# GET all
```
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo
```

# POST 
e.g. 
```
curl -X POST https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo \--data-raw '{ "title": "task ", "description": "Create todo API " }'
```

# GET by ID
e.g. 
```
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc
```
Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc

# UPDATE by ID
e.g. 
```
curl -X PUT https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc \--data-raw '{ "title": "task ", "description": "Create ToDo API "}'
```
Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc


# DELETE by ID
e.g. ```curl -X DELETE https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc```

Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc
