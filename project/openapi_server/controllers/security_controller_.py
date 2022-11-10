import jwt 
from connexion.exceptions import ProblemException
import pymongo
from pymongo import errors

conn_str = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.ewdiggs.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(conn_str)
db = client.mydata

def info_from_BearerAuth(token):
    if token :
        try:
            istheretoken = db.token.find_one({'token':token})
            if istheretoken:
                if istheretoken['status']:
                    decoded_token = jwt.decode(jwt= token,key ='secret',algorithms=["HS256"])
                    return {'decoded_token':decoded_token,'token':token}
                else:
                    raise ProblemException(status=401 ,title='error',detail='you are logged out ') 
        except jwt.exceptions.InvalidTokenError:   
            raise ProblemException(status=401 ,title='error',detail='unauthorized')    
    raise ProblemException(status=401 ,title='error',detail='unauthorized')
