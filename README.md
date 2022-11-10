## `Requirements before running the application`

1. install python and included in the path
2. open the project_9-6-2022 folder
3. Create a project environment for the Flask using the command:
   ```
   virtualenv <name of enviroment>
   ```
4. activate the enviroment using the command :
   ```
    <name of enviroment>\scripts\activate.bat
   ```
5. add to the requirments.txt the following dependencies :

   ```
   pymongo[srv]
   pyjwt
   bycrypt
   ```

6. install the dependencies using the following command:
   ```
   pip install -r requirements.txt
   ```
7. start the application using the following command:
   ```
   python -m swagger_server
   ```

## `Features`:

- A User can sign up:
- A User can login using a Email and a Password
- A User can Follow/Unfollow **(if public account)**
- RequestFollow/ApproveFollow **(if private account)**
- A User can Logout
- user can list his followers
- user can list the people that he followed
- user can cancel request
- user can delete his account
- user can reject the income request
- user can get all the users

## `User Schema` :

| `Label`                | `Type` | `Default` | `Comment`                                                                                                           |
| ---------------------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------- |
| FirstName              | string | -         | no special characters or numbers are allowed.                                                                       |
| LastName               | string | -         | no special characters or numbers are allowed                                                                        |
| Email                  | string | -         | must have an email format                                                                                           |
| password               | string | -         | Minimum eight characters, at least one uppercase letter, one lowercase letter, one number and one special character |
| age                    | int    | -         | minimum age must be 18                                                                                              |
| accounttype            | string | -         | account type ; public or private                                                                                    |
| followers              | array  | []        | list of followers id                                                                                                |
| following              | array  | []        | list of you users id that you followed                                                                              |
| SentRequestsFollow     | array  | []        | list of users id with private account and you sent them follow request                                              |
| RecievedRequestsFollow | array  | []        | list of users id that sent you a follow request and waiting to be aproved                                           |
| status                 | boolen | false     | status ; false or true                                                                                              |
| gender                 | string | male      | enum ; male or female                                                                                               |

# `Functionality:`

<details>

<summary>signup</summary>

**Description:**
this api is used to create a new user.

**workflow:**

1. run the server
2. add a json object to requestbody including (email ,password,firstname ,lastname,accountype,gender,age )
3. call the url
   ```
   localhost:8070/signup
   ```

**constraints:**

1. email should not match an existence email
2. input credential must be validate

**URL** : `/signup`

**Method** : `POST`

**Auth required** : NO

**login required** : NO

**Requestbody Data example**

```json
{"message": "string",
   "user_info" : {
  "Email": "user@example.com",
  "password": "BQGAw7nITTLIP5QVmh",
  "FirstName": "OGBZBwrqN--DpjW",
  "LastName": "rMI-I,cSi-HvpnH",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18
}}
```

## Success Response

**Code** : `201 created`

</details>

<details>
<summary>login</summary>

**constraints:**

1. email and password must be authorized

**Description:**
this api is used to login

**workflow:**

1. run the server
2. add a json object to requestbody including (email ,password )
3. call the url
   ```
   localhost:8070/login
   ```

**URL** : `/login`

**Method** : `POST`

**Auth required** : NO

**login required** : NO

**Requestbody Data example**

```json
{
  "Email": "user@example.com",
  "password": "BQGAw7nITTLIP5QVmh"
}
```

## Success Response

**Code** : `200 login sucessfully`

**Content examples**

```json
{
   "token": "dfsfsfsfsfs",
   {
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}
}
```

</details>

<details>
<summary>logout</summary>

**Description:**
this api is used to logout

**workflow:**

1. run the server
2. add the token to the authorization header
3. call the url
   ```
   localhost:8070/logout
   ```

**URL** : `/logout`

**Method** : `POST`

**Auth required** : YES

**login required** : YES

**Requestbody Data example**

```json
{
  "_id": "vxcvxfdfsfsfsfsfs" // id of user
}
```

## Success Response

**Code** : `200 logout sucessfully`
```json
{
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}
```
</details>

<details>
<summary>follow a user</summary>

**Description:**
this api is used to create a follow a public user.

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. add the id of the user you want to follow in the requestbody
4. call the url
   ```
   localhost:8070/user/follow
   ```

**URL** : `/follow`

**Method** : `patch`

**Auth required** : YES

**login required** : YES

**Requestbody Data example**

```json
{
  "_id": "zvzgvdxvfdsfd" // id of the user you want to follow
}
```

## Success Response

**Code** : `200 sucessfully followed a user`
```json
{"message": "string",
   "user_info" : {
  "Email": "user@example.com",
  "password": "BQGAw7nITTLIP5QVmh",
  "FirstName": "OGBZBwrqN--DpjW",
  "LastName": "rMI-I,cSi-HvpnH",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18
}}
```

</details>

<details>
<summary>unfollow a user</summary>

**Description:**
this api is used to unfollow a user

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. add the id of the user you want to unfollow in the requestbody
4. call the url
   ```
   localhost:8070/unfollow
   ```

**URL** : `/unfollow`

**Method** : `patch`

**Auth required** : YES

**login required** : YES

**Requestbody Data example**

```json
{
  "_id": "sfsfsdgsdgsdgsdgsdg" // id of the user you want to unfollow
}
```

## Success Response

**Code** : `200 sucessfully followed a user`
```json
{"message": "string",
   "user_info" : {
  "Email": "user@example.com",
  "password": "BQGAw7nITTLIP5QVmh",
  "FirstName": "OGBZBwrqN--DpjW",
  "LastName": "rMI-I,cSi-HvpnH",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18
}}
```
</details>

<details>
<summary>request follow </summary>

**Description:**
this api is used to sent a private account a follow request

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. add the id of the user you want to follow in the requestbody
4. call the url
   ```
   localhost:8070/user/requestfollow
   ```

**URL** : `/user/requestfollow`

**Method** : `patch`

**Auth required** : YES

**login required** : YES

**Requestbody Data example**

```json
{
  "_id": "dfsfsgsgsdgsgsgsg" // id of the user you want to follow
}
```

## Success Response

**Code** : `200 sucessfully sent the request `
```json
{
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}
```
</details>

<details>
<summary>approve follow </summary>

**Description:**
this api is used approve a recived follow request.

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. add the id of the user that sent you the request in the requestbody
4. call the url
   ```
   localhost:8070/user/aprovefollow
   ```

**URL** : `/user/approvefollow`

**Method** : `patch`

**Auth required** : YES

**login required** : YES

**Requestbody Data example**

```json
{
  "_id": "dfsfsgsgsdgsgsgsg" // id of the user you want to follow
}
```

## Success Response

**Code** : `200 sucessfully approved the request `
```json
{
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}
```
</details>

<details>
<summary>get a user </summary>

**Description:**
this api is get the user info .

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. add the id of the user in the path
4. call the url
   ```
   localhost:8070/{user_id}
   ```

**URL** : `/{user_id}`

**Method** : `get`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 ok `

**Content examples**

```json
{
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}
```

</details>












<details>
<summary>reject a request </summary>

**Description:**
this api is used to reject a request .

**workflow:**

1. run the server
2. add the the token that was given after login to authorization headerh
3. call the url
   ```
   localhost:8070/Rejectfollow
   ```

**URL** : `/user/Rejectfollow`

**Method** : `Patch`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 ok `

**Content examples**

```json
{

   "message" : "string",
   "user_info" : {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}}
```

</details>

















<details>
<summary>cancel a request </summary>

**Description:**
this api is used cancel  a follow request .

**workflow:**

1. run the server
2. add the the token that was given after login to authorization headerh
3. call the url
   ```
   localhost:8070/cancelfollow
   ```

**URL** : `/user/cancelfollow`

**Method** : `Patch`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 ok `

**Content examples**

```json
{

   "message" : "string",
   "user_info" : {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}}
```

</details>





<details>
<summary>delete account</summary>

**Description:**
this api is used to delete your account .

**workflow:**

1. run the server
2. add the the token that was given after login to authorization headerh
3. call the url
   ```
   localhost:8070/DeletetAccount
   ```

**URL** : `/user/DeletetAccount`

**Method** : `Patch`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 ok `

**Content examples**

```json
{

   "message" : "string",
   "user_info" : {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}}
```

</details>



























<details>
<summary>get your all users </summary>

**Description:**
this api is used to get all users

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. call the url
   ```
   localhost:8070/getall
   ```

**URL** : `/user/getall

**Method** : `get`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 successfully get all users `

**Content examples**

```json


{   " message" : "string",

      "users":  [ {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}]
}
```



</details>








































<details>
<summary>get your all followers </summary>

**Description:**
this api is used to get the the user's id that followed you.

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. call the url
   ```
   localhost:8070/user/followers
   ```

**URL** : `/user/followers

**Method** : `get`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 successfully get all followers `

**Content examples**

```json


{   " message" : "string",

      "users":  [ {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}]
}
```



</details>

<details>
<summary>get your all following </summary>

**Description:**
this api is used to get the the user's id that you followed.

**workflow:**

1. run the server
2. add the the token that was given after login to authorization header
3. call the url
   ```
   localhost:8070/user/following
   ```

**URL** : `/user/following`

**Method** : `get`

**Auth required** : YES

**login required** : YES

## Success Response

**Code** : `200 successfully get all following `

**Content examples**

```json


{   " message" : "string",

      "users":  [ {
   "_id" : "rtetetetetet",
  "Email": "user@example.com",
  "password": "qw8kuvX4kuJZzxPMGo0E2ES9bHY17X!IcvMPDB6xjb!xI3$@Wk9sNTOfZ",
  "FirstName": "bzEWZNqtDcuVeLx",
  "LastName": "rXC'BKk,vRJjyT,",
  "AccountType": "private",
  "Gender": "male",
  "Age": 18,
  "status": "loggedin"
}]
}
```

</details>

## `Authentication/Authorization :`

the token type is jwt

`when you signup the `password is hashed and saved in database

`when you login` the server response with json having a token with expiration date and a session is created

`when you logout` the session is removed

`when you try to call any api` the server checks if the token is valid, not expired. andlogged in .

## `Challenges : `

the most challenge was the logout process beacuse i was confused if logout must be done at the client side but then i used session in cookies
