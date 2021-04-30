# &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Python Developer Test

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
```
    1.Register
    
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
              }
``` 
             
              
              
![Screenshot (24)](https://user-images.githubusercontent.com/51699297/116748995-e6547400-aa1d-11eb-80eb-4d1e65479861.png)



``` 
    2) Login

    URL : localhost:5000/login
    Method : POST
    Headers : {
                 'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                email : 'lead_test@subi.com',
                password : '123456'
              } 
```
![Screenshot (25)](https://user-images.githubusercontent.com/51699297/116749020-f3716300-aa1d-11eb-838e-afd9ee9728f9.png)


```
    3)Insert new Template

    URL : locahost:5000/template

    Method : POST
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
                     } 
```
Header formation
![Screenshot (27)](https://user-images.githubusercontent.com/51699297/116749120-1865d600-aa1e-11eb-8965-c6f0a0f9fabe.png)


body
![Screenshot (29)](https://user-images.githubusercontent.com/51699297/116749167-27e51f00-aa1e-11eb-8bd1-32c6919b7567.png)



```
    4.Get All Template

    URL : locahost:5000/template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  
```

 
![Screenshot (30)](https://user-images.githubusercontent.com/51699297/116749254-4c40fb80-aa1e-11eb-91a1-ba39eb455067.png)

```
    5.GET Single Template

    URL : locahost:5000/template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
Body :    {} 
```


c
![Screenshot (31)](https://user-images.githubusercontent.com/51699297/116749302-5cf17180-aa1e-11eb-92ef-a8eeeb56510a.png)



``` 
    6.Update Single Template

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
}   
```


![Screenshot (32)](https://user-images.githubusercontent.com/51699297/116749342-6da1e780-aa1e-11eb-9858-ff26d5fa72f8.png)


![Screenshot (33)](https://user-images.githubusercontent.com/51699297/116749394-7db9c700-aa1e-11eb-8606-348f478d2403.png)


``` 
    7.DELETE Single Template

    URL : locahost:5000/template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  
```

![Screenshot (34)](https://user-images.githubusercontent.com/51699297/116749411-86aa9880-aa1e-11eb-9e64-a4e80cc08683.png)


