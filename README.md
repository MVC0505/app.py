Flask REST API — User Management

This project is a simple RESTful API built using Flask. It provides endpoints to manage user data with full CRUD (Create, Read, Update, Delete) functionality. Data is stored in an in-memory Python dictionary for easy demonstration and testing.

- Features

    GET all users

    GET a single user by ID

    POST a new user

    PUT (update) an existing user

    DELETE a user

    Input validation and error handling

- Technologies Used

    Python

    Flask

    Postman or cURL (for testing)

- Installation
1. Install Dependencies

        pip install flask

2. Run the Application

        python app.py


      The server will start at:

        http://127.0.0.1:5000/

- API Endpoints
1. Get All Users

    GET /users

    Returns all users in the system.

2. Get User by ID

    GET /users/<id>

    Example:

        GET /users/1

3. Create New User

    POST /users

    JSON Body Example:

        {
           "name": "John Doe",
           "email": "john@example.com"
        }

4. Update Existing User

    PUT /users/<id>

    JSON Body Example:

        {
          "email": "newemail@example.com"
        }

5. Delete a User

    DELETE /users/<id>

    Example:

        DELETE /users/1
  
- Testing with Postman or cURL

  GET all users

      curl http://127.0.0.1:5000/users

  GET a specific user

      curl http://127.0.0.1:5000/users/1

  POST (Create user)

        curl -X POST -H "Content-Type: application/json" \
        -d "{\"name\":\"Alice\", \"email\":\"alice@example.com\"}" \
        http://127.0.0.1:5000/users

  PUT (Update user)

       curl -X PUT -H "Content-Type: application/json" \
        -d "{\"email\":\"updated@example.com\"}" \
        http://127.0.0.1:5000/users/1

  DELETE (Remove user)

        curl -X DELETE http://127.0.0.1:5000/users/1
