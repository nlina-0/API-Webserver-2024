
### Create/Register User
```
"/users/register", methods=["POST]
```

###### Body
```
  "name": "",
  "email": "",
  "password": "" 
```

###### Response
```
  "email": "",
  "id": ,
  "is_admin": ,
  "name": "",
  "password": ""
```

<br></br>

### User Login
```
"/users/login", methods=["POST"]
```

###### Body
```
  "email": "",
  "password": ""
```

###### Response
```
    "token":
```

<br></br>

### Get all Users: Admin only
User must be logged in as admin to perform any 'admin only' endpoints.
```
/users/, methods=["GET"]
```

###### Header data??
```
Bearer Token: "token"
```

###### Response
```
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

```
@users_bp.route("/<int:id>", methods=["DELETE"])
```
###### Header data??
```
user_id:
```