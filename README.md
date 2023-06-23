Hello, my name is Anastasiia 

lambda_function.py is the code currently running on AWS Lambda. To test the functionality you can run examples from below in the terminal

# GET all
Get the list of all the ToDo tasks 
```
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo
```

# POST 
Create a ToDo task
e.g. 
```
curl -X POST https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo \--data-raw '{ "title": "Here is your task title", "description": "Here is your task description" }'
```

# GET by ID
Get a ToDo task, using its ID
e.g. 
```
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc
```
Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc

# UPDATE by ID
Update already existing ToDo task using its ID
e.g. 
```
curl -X PUT https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc \--data-raw '{ "title": "The new title is here ", "description": "The new description is here "}'
```
Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc


# DELETE by ID
Delete a ToDo task using its ID
e.g. 
```
curl -X DELETE https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/3e58beaf-3cb1-402a-991a-8e31670207cc
```

Here: ID = 3e58beaf-3cb1-402a-991a-8e31670207cc
