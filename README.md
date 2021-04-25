# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python Developer Test

___
### Table of Content:
-	[About the project](#about-the-project) 
-	[Set up](#set-up)
-	[Results](#results)

# About the project:
This is a flask application using MongoDB as back-end. To make more secure connection , here I used the JWT(JSON Web Tokens) tokens for authorization. Finally testing the application using the postman.<br/>
#### <b><i>Technology used:</i></b>
- <b><i>Flask </i></b>---> Python based micro framework for creating REST API.
- <b><i>MongoDB</i></b> -> MongoDB is a document-oriented and NoSQL database solution that provides great scalability and flexibility along with a powerful querying system. 
- <b><i>JWT </i></b>-----> JWTs are a good way of securely transmitting information between parties.Additionally, the structure of a JWT allows you to verify that the content hasn't been tampered with.It Is used for the authorization not for authentication. There is a small different between those two.<br/><br/>
-- Authentication --> check the user password and username is correct and the person is already registered.<br/><br/>
-- Authorization --->  Check the request is made by the same user, who checked by the authentication process.<br/><br/>
To get the clear understanding ------> [resorces](https://en.wikipedia.org/wiki/JSON_Web_Token) , [vedio]()<br/>

# Set up:
First I need to set up the environment to get started.
- Installed python3 (above 3.6)
- Created a folder particular for the project 
- In CMD go to that project folder and using the following the command <br/>

```Python3 -m venv <name-of-your-vertual-enviranment>```
- Inside the Virtual Environment Installed the following packages.
1) flask
2)	pymongo
3)	bson
4)	json
5) sys
6) os
7) werkzeug
8) functools
9) datetime

# Results:
```1.Register
    
    URL : localhost:5000/register
    Method : POST
    Headers : {
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                first_name : 'lead_test@subi.com',
                last_name : '123456'
                email : 'lead_test@subi.com',
                password : '123456'
              }```

``` 2 Login

    URL : localhost:5000/login
    Method : POST
    Headers : {
                 'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                email : 'lead_test@subi.com',
                password : '123456'
              }  ```

``` 3.Get All Template

    URL : locahost:5000/template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  ```

``` 4.GET Single Template

    URL : locahost:5000/template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
Body :    {} ```

``` 5.Update Single Template

    URL : locahost:5000/template/<template_id>
    
    Method : PUT
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
}   ```


``` 6..DELETE Single Template

    URL : locahost:5000/template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  ```



