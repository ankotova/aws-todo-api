
# GET all
curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo

# POST 
curl -X POST https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo \\
--data-raw '{
    "title": " ",
    "description": " "
}'

# GET by ID
e.g. curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/a6840683-f090-47e5-9c95-47529d0c28bc 

Here: ID = a6840683-f090-47e5-9c95-47529d0c28bc

# UPDATE by ID
curl -X PUT https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/a6840683-f090-47e5-9c95-47529d0c28bc \\
--data-raw '{ "title": " ",  "description": " "
}'

Here: ID = a6840683-f090-47e5-9c95-47529d0c28bc


# DELETE by ID
curl -X DELETE https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/a6840683-f090-47e5-9c95-47529d0c28bc 

Here: ID = a6840683-f090-47e5-9c95-47529d0c28bc