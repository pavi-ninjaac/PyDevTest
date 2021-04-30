
import sys , os
from flask import Flask , jsonify , request , Response
import jwt
import json
from datetime import datetime , timedelta
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash , check_password_hash #password hasing 
from functools import wraps

sys.path.append(os.path.abspath('D:\SPIECBLUE_PYDEVTEST'))
#print(sys.path)
from app import app

#set the database connection
from core.MongoDBConnect import connect
db = connect().make_connection()

def jwt_token_required(func):
    @wraps(func)
    def decorated_wraper(*arg , **kwargs):
        token = None
        #f JWT token prsent in the header 
        if 'Authorization' in request.headers:
            token =  request.headers['Authorization']
            #print(token)
        if not token:
            return jsonify({"Error"  : "The JWT Token is missing...."})
        
        #decode the token
        try:
            data = jwt.decode(token , app.config['SECRET_KEY'] , algorithms="HS256")    
            #print(data)        
            cur_user = db.valid.find_one({'_id' : ObjectId(data['user']['id'])})
        except Exception as e:
            print(e)
            return jsonify({"Error"  : "The JWT Token is invalid...."})

        return func(cur_user, *arg, **kwargs)
    return decorated_wraper
#register


@app.route('/register/' , methods = ['POST'])
def register():
    j = request.json
    first_name = j['firstName']
    last_name = j['lastName']
    email = j['email']
    password = j['password']

    check_user = db.valid.find({"email" : email})
    if check_user.count() < 1:
        if first_name and last_name and email and password and request.method == 'POST':
            hased_pass = generate_password_hash(password)
            data = {'firstName' : first_name , "lastName" : last_name , "email" : email , "password" : hased_pass}
            db.valid.insert_one(data)
            return jsonify({"message"   : "User regstered Succesfully!!! :):)"})
        else:
            return jsonify({"message"  : "Carefully insert the values...some fields are mssing :( :("})
    else:
        return Response(
            response = 
            json.dumps({"message":"User with this mail id is already exits"},default=str), 
            status=401,
            mimetype="application/json"
            )


@app.route('/login/' , methods = ['POST'])
def login():
    j = request.json
    email = j['email']
    pwd = j['password']

    user = db.valid.find_one({'email' : email })
    #print(user)
    if user:
        #user['_id'] = str(user['_id'])
        if user and check_password_hash(user['password'] , pwd):
            expire_time = datetime.utcnow() + timedelta(hours= 1)
            token_user = jwt.encode({
                "user" : {
                    "email" : f"{user['email']}",
                    "id" : f"{user['_id']}"
                         },
                "exp":expire_time
                               }, 
                app.config['SECRET_KEY'],
                algorithm="HS256"
            )
            return Response(
            response = 
            json.dumps({"token_from_user":token_user},default=str), 
            status=200,
            mimetype="application/json"
            )
        
        else:
            return Response(
            response = 
            json.dumps({"message":"Wrong password ........... :( :("},default=str), 
            status=401,
            mimetype="application/json"
            )
    else:
        return Response(
            response = 
            json.dumps({"message":"Invalid Login credencials :( :("},default=str), 
            status=401,
            mimetype="application/json"
            )

@app.route('/template/' , methods = ['POST'])
@jwt_token_required
def insert_template(current_user):
    j = request.json
    login_user_id = current_user["_id"] #_id
    temaplte_name = j['temaplte_name']
    subject = j['subject']
    body = j['body']

    
    
    if login_user_id and temaplte_name and subject and body and request.method == 'POST':
            
            data = {'login_user_id' : login_user_id , "temaplte_name" : temaplte_name , "subject" : subject , "body" : body}
            db.templates.insert_one(data)
            return Response(
                response = 
                json.dumps({"message":"Templated added to user account!!! :):)"},default=str), 
                status=401,
                mimetype="application/json"
                 )
    else:
            return Response(
                response = 
                json.dumps({"message":"Carefully insert the values...some fields are mssing :( :("},default=str), 
                status=401,
                mimetype="application/json"
                 )
    

    


@app.route('/template/' , methods = ['GET'])
@jwt_token_required
def get_all_user(current_user):
    try:
        #get the current user data only
        current_login_user_id = current_user["_id"]
        data_all_users = list(db.templates.find({"login_user_id" : current_login_user_id}))
        

        res = Response(
            response = json.dumps(data_all_users , default = str),
            status = 200,
            mimetype = "application/json"
        )
        return res
    except Exception as e:
        print("error in get all datae",e)
        return Response(
            response = 
            json.dumps({"message":"Can't get the data from the DataBase"},default=str), 
            status=404,
            mimetype="application/json"
            )

@app.route('/template/<id>/' , methods = ['GET'])
@jwt_token_required
def get_user(current_user,id):
    #get the spesific users templates only

    user_found = db.templates.find_one({"_id" : ObjectId(id)})
    
    if user_found:
        current_login_user_id = current_user["_id"]
        user_found_login_id = user_found["login_user_id"]
        #print('user poth are same')
        if current_login_user_id == user_found_login_id:
            try:
                single_user = db.templates.find_one({'_id' : ObjectId(id)})
                
                res = Response(
                    response = json.dumps(single_user , default = str),
                    status = 200,
                    mimetype = "application/json"
                )
                return res
            except Exception as e:
                print("error in get all datae",e)
                return Response(
                    response = 
                    json.dumps({"message":"Can't get the data from the DataBase"},default=str), 
                    status=404,
                    mimetype="application/json"
                    )
        else:
            return Response(
                            response = 
                            json.dumps({"message":"You Don't have permission to view this records...........!!!!!!"},default=str), 
                            status=404,
                            mimetype="application/json"
                            )
    else:
            return Response(
                            response = 
                            json.dumps({"message":"THERE is no Template with this id....."},default=str), 
                            status=404,
                            mimetype="application/json"
                            )
    


@app.route('/template/<id>/' , methods = ['PUT'])
@jwt_token_required
def update_one_user(current_user,id):

    j = request.json
    login_user_id = current_user["_id"] #_id
    temaplte_name = j['temaplte_name']
    subject = j['subject']
    body = j['body']
        
    user_found = db.templates.find_one({"_id" : ObjectId(id)})
    
    if user_found:
        current_login_user_id = current_user["_id"]
        user_found_login_id = user_found["login_user_id"]
        #print('user poth are same')
        if current_login_user_id == user_found_login_id:
            if login_user_id and temaplte_name and subject and body and request.method == 'PUT':
                try:
                    
                    db.templates.update_one({'_id':ObjectId(id['$oid']) if '$oid' in id else ObjectId(id) } , {'$set' : {'login_user_id' : login_user_id , "temaplte_name" : temaplte_name , "subject" : subject , "body" : body}})
                    res = Response(
                        
                            response = json.dumps({"message" : "Template updated Successfully!!! :) :) :)"} , default=str),
                            status=200,
                            mimetype="application/json"
                        
                    )
                    return res
            
                except Exception as e:
                    print("error in update datas",e)
                    return Response(
                        response = 
                        json.dumps({"message":"Can't update the data from the DataBase"},default=str), 
                        status=404,
                        mimetype="application/json"
                        )
            else:
                return Response(
                        response = 
                        json.dumps({"message":"Enter all fields carefully...some fields are missing"},default=str), 
                        status=404,
                        mimetype="application/json"
                        )
        else:
            return Response(
                        response = 
                        json.dumps({"message":"You Don't have permission to EDIT this records...........!!!!!!"},default=str), 
                        status=404,
                        mimetype="application/json"
                        )
    else:
            return Response(
                        response = 
                        json.dumps({"message":"THERE is no Template with this id....."},default=str), 
                        status=404,
                        mimetype="application/json"
                        )
    



@app.route('/template/<id>/' , methods = ['DELETE'])
@jwt_token_required
def delete_user(current_user,id):
    
    user_found = db.templates.find_one({"_id" : ObjectId(id)})
    
    if user_found:
        current_login_user_id = current_user["_id"]
        user_found_login_id = user_found["login_user_id"]
        
        if current_login_user_id == user_found_login_id:
            try:
                db.templates.delete_one({"_id" : ObjectId(id)})
                return Response(
                    response = 
                    json.dumps({"message":"Recort deleted successflly!!!!!"},default=str), 
                    status=200,
                    mimetype="application/json"
                    )
        
            except Exception as e:
                print("error in get all datae",e)
                return Response(
                    response = 
                    json.dumps({"message":"Can't delete the data from the DataBase"},default=str), 
                    status=404,
                    mimetype="application/json"
                    )
        else:
            return Response(
                        response = 
                        json.dumps({"message":"You Don't have permission to DELETE this records...........!!!!!!"},default=str), 
                        status=404,
                        mimetype="application/json"
                        )
    
    else:
            return Response(
                    response = 
                    json.dumps({"message":"There is not template with this id........."},default=str), 
                    status=404,
                    mimetype="application/json"
                    )
