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
             
              
              
![Screenshot (348)](https://user-images.githubusercontent.com/51699297/115988209-2e1a6c00-a5d6-11eb-864d-54570e0a3a59.png)


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
![Screenshot (350)](https://user-images.githubusercontent.com/51699297/115988305-ada83b00-a5d6-11eb-9495-0f04f45ce856.png)

```
    3.Get All Template

    URL : locahost:5000/template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  
```



![Screenshot (351)](https://user-images.githubusercontent.com/51699297/115988890-34f6ae00-a5d9-11eb-867b-ebc5245c0222.png)



```
    4.GET Single Template

    URL : locahost:5000/template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
Body :    {} 
```



![Screenshot (352)](https://user-images.githubusercontent.com/51699297/115988893-37f19e80-a5d9-11eb-9688-d9cd699b879d.png)



``` 
    5.Update Single Template

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


![Screenshot (353)](https://user-images.githubusercontent.com/51699297/115988894-3922cb80-a5d9-11eb-8b4d-7b872d95e092.png)



``` 
    6..DELETE Single Template

    URL : locahost:5000/template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  
```

![Screenshot (354)](https://user-images.githubusercontent.com/51699297/115989305-5c4e7a80-a5db-11eb-9c0c-211807d53149.png)


