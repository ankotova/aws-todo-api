
# GET all
' curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo '

# POST 
curl -X POST https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo \\--data-raw '{ "title": "task ", "description": "Create todo API " }'

# GET by ID
e.g. curl https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/796aefbb-1088-42d0-a987-7a8156204853

Here: ID = 796aefbb-1088-42d0-a987-7a8156204853

# UPDATE by ID
curl -X PUT https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/796aefbb-1088-42d0-a987-7a8156204853 \\--data-raw '{ "title": "task ", "description": "Create ToDo API "}'

Here: ID = 796aefbb-1088-42d0-a987-7a8156204853


# DELETE by ID
curl -X DELETE https://jtnw4u2muj.execute-api.eu-central-1.amazonaws.com/v1/todo/796aefbb-1088-42d0-a987-7a8156204853 

Here: ID = 796aefbb-1088-42d0-a987-7a8156204853
