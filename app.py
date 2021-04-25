from flask import Flask , jsonify , Response
import json
#import the app from the __init__.py from core directory
from core import app

# import all the routers from the routes file in core directory
from core import routes

#handle the 404 error here
@app.errorhandler(404)
def pageNotFound(error):
    return Response(
                    response = 
                    json.dumps({"message":"No such route(page) is available........."},default=str), 
                    status=404,
                    mimetype="application/json"
                    )

#run the flask app
if __name__ == "__main__":
    app.run(debug=True , port=3000)