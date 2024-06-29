
### Create/Register User
Anyone can create an account.
```py
"/users/register", methods=["POST]
```

###### Body: All fields are required
```py
  "name": "",
  "email": "",
  "password": "" 
```

###### Response
```py
  "email": "",
  "id": ,
  "is_admin": ,
  "name": "",
  "password": ""
```

<br></br>

### User Login
```py
"/users/login", methods=["POST"]
```

###### Body: All fields are required
```py
  "email": "",
  "password": ""
```

###### Response
```py
    "token":
```

<br></br>

### Get all Users: Admin only
User must be logged in as admin to perform any 'admin only' endpoints.
```py
"/users", methods=["GET"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Response
```py
[
  {
    "email": "",
    "id": ,
    "is_admin": ,
    "name": 
  }
]
  ```

  <br></br>

  ### Delete User: Admin only
  Admin needs to enter user_id of the user in http request to delete user. User_id can be found in 'get all users' endpoint.

``` py
"users/<int:id>", methods=["DELETE"]
```

###### Header data
```py
user_id: int
```
```py
Bearer Token: "token"
```

 <br></br>

  ### Update User - double check !!
  User has to be logged in and can only update their own account. Fields that can be updated are name, email and password.

``` py
"/users", methods=["PUT", "PATCH"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Body: All fields are optional
```py
{
  "name": "",
  "email": "",
  "password": ""
}
```

###### Response
```py
{
  "email": "",
  "id": ,
  "is_admin": ,
  "name": "",
  "password": ""
}
```

<br></br>

### Get all Exercises
Available to everyone.
```py
"/exercises", methods=["GET"]
```

###### Response
```py
[
  {
    "description": "",
    "exercise": "",
    "exercise_id": 
  },
  {
    "description": "",
    "exercise": "",
    "exercise_id": 
  }
]
  ```

  <br></br>

### Get one Exercise
Available to everyone. A specific exercise can be requested by enterting the exericse_id in the http request. Exercise_id for each exercise can be found in the 'get all exercises' endpoint.
```py
"/exercises/<int:id>", methods=["GET"]
```

###### Header data
```py
exercise_id: int
```

###### Response
```py
[
  {
    "description": "",
    "exercise": "",
    "exercise_id": 
  },
  {
    "description": "",
    "exercise": "",
    "exercise_id": 
  }
]
  ```

  <br></br>

  ### Create Exercise: Admin only
  Only the admin can create an exercise to add to the library of exercises. Both exercise name and description are required. 
```py
"/users", methods=["POST]
```

###### Header data
```py
Bearer Token: "token"
```

###### Body: All fields are required
```py
{
  "name": "",
  "description": ""
}
```

###### Response
```py
{
  "description": "",
  "exercise": "",
  "exercise_id": 
}
```

 <br></br>

  ### Update Exercise: Admin only
``` py
"/exercises/<int:id>", methods=["PUT", "PATCH"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Body: All fields are optional
```py
{
  "name": "",
  "description": ""
}
```

###### Response
```py
{
  "email": "",
  "id": ,
  "is_admin": ,
  "name": "",
  "password": ""
}
```

<br></br>

### Delete Exercise: Admin only
  Admin needs to enter exercise_id in http request to delete exercise. Exercise_id can be found in 'get all exercises' endpoint.

``` py
"/exercises/<int:id>", methods=["DELETE"]
```

###### Header data
```py
user_id: int

Bearer Token: "token"
```

<br></br>

### Get all Sessions
If logged in as admin, admin will get all sessions. If logged in as client user, user will only get sessions owned by them. This endpoint provides users with an overview of all workout sessions completed.
```py
"/sessions", methods=["GET"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Response
```py
[
  {
    "date": "",
    "session_id": ,
    "user": {
      "id": ,
      "name": ""
    }
  },
  {
    "date": "",
    "session_id": ,
    "user": {
      "id": ,
      "name": ""
    }
  }
]
  ```

<br></br>

### Get one Session by ID
Admin can access all sessions. User can only access sessions owned by them. This endpoint allows users to see more information about a specific session. More information includes, exercises performed, sets, weights and repitions completed for each exercise. The session_id which can be found in the 'get all sessions' endpoint is required in the http request. 
```py
"/sessions/<int:session_id>", methods=["GET"]
```

###### Header data
```py
exercise_id: int

Bearer Token: "token"
```

###### Response
```py
{
  "date": "",
  "session_id": ,
  "session_sets": [
    {
      "exercise_name": "",
      "exercise_set": ,
      "id": ,
      "reps": ,
      "weight": 
    }
  ]
]
  ```

###### Failed Responses
  If a user enters a session_id they do not own:
  ```py
Status code: 403

{
  "error": "You must be the owner to access this resource"
}
```

If a user or admin enters a session that does not exist:
  ```py
Status code: 404

{
  "error": "Not Found"
}
```

 <br></br>

### Create Sessions
  Anyone with an account and is logged in can create a session. This endpoint will update the database with a new session_id with the days date. No body is required. 
```py
"/sessions", methods=["POST"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Response
```py
{
  "date": "",
  "session_id": ,
  "session_sets": [],
  "user": {
    "id": ,
    "name": ""
  }
}
```

###### Failed Responses
If no one is logged in:
```py
Status code: 422

{
  "msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```

<br></br>

### Delete Session
  Either the admin or owner of the session can delete a session. The session_id must be entered in the HTTP request. Session sets assigned to session will also be deleted.

``` py
"/sessions/<int:id>", methods=["DELETE"]
```

###### Header data
```py
session_id: int

Bearer Token: "token"
```

###### Failed Responses
If the user does not own the session:
```py
Status code: 403

{
  "error": "You must be the owner to access this resource"
}
```

If the session does not exist:
```py
Status code: 404

{
  "error": "Not Found"
}
```

<br></br>

### Get a Session Set
Admin can access all sessions sets. User can only access sessions sets owned by them. This endpoint allows to retrive all the information about one specific exercise they've completed by entering the session set id in the HTTP request. Session set id's can be found in sessions.
```py
"/session-sets/<int:id>", methods=["GET"]
```

###### Header data
```py
id: int

Bearer Token: "token"
```

###### Response
```py
{
  "exercise_name": "",
  "exercise_set": ,
  "id": ,
  "reps": ,
  "session": {
    "date": "",
    "session_id": 
  },
  "weight": 
}
  ```

###### Failed Responses
If the user does not own the session set:
```py
Status code: 403

{
  "error": "You must be the owner to access this resource"
}
```
If the session set does not exist:
```py
Status code: 404

{
  "error": "Not Found"
}
```

<br></br>

### Create Session Set
  User has to be logged in. User must own the latest session to create a session set. To be the latest ownder of a session, the user must create one.  
```py
"/session-sets", methods=["POST"]
```

###### Header data
```py
Bearer Token: "token"
```
###### Body: All fields are required
```py
{
  "exercise_set": "",
  "exercise_name": "",
  "reps": "",
  "weight": ""
}
```

###### Response
```py
{
  "date": "",
  "session_id": ,
  "session_sets": [],
  "user": {
    "id": ,
    "name": ""
  }
}
```

###### Failed Responses
If no one is logged in:
```py
Status code: 422

{
  "msg": "Bad Authorization header. Expected 'Authorization: Bearer <JWT>'"
}
```

If field in body is missing: 
```py
Status code: 400

{
  "error": {
    "field: [
      "Missing data for required field."
    ]
  }
}
```
If user does not own the latest session:
```py
Status code: 403

{
  "error": "You must be the session owner. Create a new session to become session owner."
}
```

<br></br>

### Update Session Set - double check !!
Admin or user must be logged in. Admin can update any session set, user can only update session set they own. 
``` py
"/session-sets/<int:id>", methods=["PUT", "PATCH"]
```

###### Header data
```py
Bearer Token: "token"
```

###### Body: All fields are optional
```py
{
  "name": "",
  "description": ""
}
```

###### Response
```py
{
  "email": "",
  "id": ,
  "is_admin": ,
  "name": "",
  "password": ""
}
```

<br></br>

### Delete Session Set
Either the admin or owner of the session set can delete a session set. The session_set_id must be entered in the HTTP request.

``` py
"/session-sets/<int:id>", methods=["DELETE"]
```

###### Header data
```py
session_set_id: int

Bearer Token: "token"
```

###### Failed Responses
If the user does not own the session set:
```py
Status code: 403

{
  "error": "You must be the owner to access this resource"
}
```

If the session set does not exist:
```py
Status code: 404

{
  "error": "Not Found"
}
```