
# GET all
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo

# POST 
curl -X POST https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo \\--data-raw '{ "title": "task ", "description": "Create todo API " }'

# GET by ID
e.g. curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/7e6638e2-e38a-4ada-a9d8-e77de38e2d54

Here: ID = 7e6638e2-e38a-4ada-a9d8-e77de38e2d54

# UPDATE by ID
curl -X PUT https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/7e6638e2-e38a-4ada-a9d8-e77de38e2d54 \\--data-raw '{ "title": "task ", "description": "Create ToDo API "}'

Here: ID = 7e6638e2-e38a-4ada-a9d8-e77de38e2d54


# DELETE by ID
ccurl -X DELETE https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/7e6638e2-e38a-4ada-a9d8-e77de38e2d54 

Here: ID = 7e6638e2-e38a-4ada-a9d8-e77de38e2d54
