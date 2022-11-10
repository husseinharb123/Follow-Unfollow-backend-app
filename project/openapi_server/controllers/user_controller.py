import datetime
import connexion
import bcrypt
from connexion.exceptions import ProblemException
from flask import *
import pymongo
from pymongo import errors
import jwt
from bson import json_util, ObjectId
import json
conn_str = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.ewdiggs.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(conn_str)
db = client.mydata

from openapi_server.models.approve_follow_response import ApproveFollowResponse  # noqa: E501
from openapi_server.models.cancel_request_response import CancelRequestResponse  # noqa: E501
from openapi_server.models.delete_account_response import DeleteAccountResponse  # noqa: E501
from openapi_server.models.follow_response import FollowResponse  # noqa: E501
from openapi_server.models.get_all_response import GetAllResponse  # noqa: E501
from openapi_server.models.get_followers_response import GetFollowersResponse  # noqa: E501
from openapi_server.models.get_following_response import GetFollowingResponse  # noqa: E501
from openapi_server.models.get_user_response import GetUserResponse  # noqa: E501
from openapi_server.models.login_request import LoginRequest  # noqa: E501
from openapi_server.models.login_response import LoginResponse  # noqa: E501
from openapi_server.models.logout_response import LogoutResponse  # noqa: E501
from openapi_server.models.rejectfollow_response import RejectfollowResponse  # noqa: E501
from openapi_server.models.requestfollow_response import RequestfollowResponse  # noqa: E501
from openapi_server.models.signup_response import SignupResponse  # noqa: E501
from openapi_server.models.unfollow_response import UnfollowResponse  # noqa: E501
from openapi_server.models.user_id import UserId  # noqa: E501
from openapi_server.models.user_info import UserInfo  # noqa: E501
from openapi_server import util

def CheckIfexist(user_ID,list):
        for each in list:
            if str(each) == user_ID: 
                return True
        return False


def approvefollow(follower_ID=None): 
    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        follower_ID = connexion.request.get_json()["_id"]
        if follower_ID and user_id:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                follower_info = db.users.find_one({"_id": ObjectId(follower_ID)})
                if follower_info:
                    if user_info['AccountType'] == 'private':                      
                        if  CheckIfexist(follower_ID,user_info['PendingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='you had sent before a follow request')   
                        if CheckIfexist(follower_ID,user_info['Following']) or CheckIfexist(follower_ID,user_info['Followers']):
                            raise  ProblemException(status=409,title='conflict',detail='you already one of his followers/following')
                        if  not CheckIfexist(follower_ID,user_info['IncomingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='the user didnt sent you a follow request')       
                        t1=db.users.update_one({"_id": ObjectId(follower_ID)},{"$push":{'Following':ObjectId(user_id) },"$pull":{'PendingFollow':ObjectId(user_id)}})  
                        t2 =db.users.update_one({"_id": ObjectId(user_id)},{"$push":{'Followers':ObjectId(follower_ID)},"$pull":{'IncomingFollow':ObjectId(follower_ID)}}) 
                        if t1.modified_count != 0 and t2.modified_count != 0:
                                return ApproveFollowResponse(
                                    message="User Aproved the Follow Request successfully",user_info=UserInfo(
                                    id= str(follower_info['_id']),
                                    email=follower_info['Email'],
                                    first_name=follower_info['FirstName'],
                                    last_name=follower_info['LastName'],
                                    age= follower_info['Age'],
                                    account_type=follower_info['AccountType'],
                                    gender=follower_info['Gender'],
                                    )),200 
                    raise ProblemException(status=409,title='error',detail='you cannot perform such request if your account is  public account' )
                raise ProblemException(status=404,title='error',detail='no user found') 
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
        raise ProblemException(status=400 ,title='error',detail='Bad Request')

def cancel_request(user_id=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        follower_ID = connexion.request.get_json()["_id"]
        if follower_ID and user_id:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                follower_info = db.users.find_one({"_id": ObjectId(follower_ID)})
                if follower_info:               
                    if CheckIfexist(follower_ID,user_info['Following']) or CheckIfexist(follower_ID,user_info['Followers']):
                        raise  ProblemException(status=409,title='conflict',detail='you already one of his followers/following')
                    if user_info['AccountType'] == 'private': 
                        if   CheckIfexist(follower_ID,user_info['IncomingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='the user  sent you before a follow request')     
                    if   not CheckIfexist(follower_ID,user_info['PendingFollow']):
                        raise  ProblemException(status=409,title='conflict',detail='you have not sent any follow request before')    
                    t1=db.users.update_one({"_id": ObjectId(follower_ID)},{"$pull":{'IncomingFollow':ObjectId(user_id)}})  
                    t2 =db.users.update_one({"_id": ObjectId(user_id)},{"$pull":{'PendingFollow':ObjectId(follower_ID)}}) 
                    if t1.modified_count != 0 and t2.modified_count != 0:
                        return CancelRequestResponse(
                            message="User canceled the Follow Request successfully",user_info=UserInfo(
                            id= str(follower_info['_id']),
                            email=follower_info['Email'],
                            first_name=follower_info['FirstName'],
                            last_name=follower_info['LastName'],
                            age= follower_info['Age'],
                            account_type=follower_info['AccountType'],
                            gender=follower_info['Gender'],
                            )),200 
                raise ProblemException(status=404,title='error',detail='no user found') 
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
        raise ProblemException(status=400 ,title='error',detail='Bad Request')

def delete_account(body=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    token = connexion.context['token_info']['token']
    user_id = tokenpayload['_id']
    if user_id :
        try:
            user_info = db.users.delete_one({"_id": ObjectId(user_id)})
            if user_info.deleted_count>0:
                return DeleteAccountResponse(message="User Delted the account successfully",user_info=UserInfo(
                        id= tokenpayload['_id'],
                        email=tokenpayload['Email'],
                        first_name=tokenpayload['FirstName'],
                        last_name=tokenpayload['LastName'],
                        age= tokenpayload['Age'],
                        account_type=tokenpayload['AccountType'],
                        gender=tokenpayload['Gender'],
                    )),200
            
            raise ProblemException(status=404,title='error',detail='no user found') 
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def follow(SentRequestTo=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        SentRequestTo = connexion.request.get_json()["_id"]
        if SentRequestTo and user_id !=SentRequestTo:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                sentto_info = db.users.find_one({"_id": ObjectId(SentRequestTo)})
                if sentto_info :
                    if sentto_info['AccountType'] == 'public' and user_info !=SentRequestTo:
                        if user_info['AccountType'] == 'private':                         
                            if  CheckIfexist(SentRequestTo,user_info['IncomingFollow']):
                                raise  ProblemException(status=409,title='conflict',detail='you cannot send follow request if he already sent you a request')    
                        if CheckIfexist(SentRequestTo,user_info['Following']) or CheckIfexist(SentRequestTo,user_info['Followers']):
                            raise  ProblemException(status=409,title='conflict',detail='you already one of his followers/following')              
                        t1=db.users.update_one({"_id": ObjectId(SentRequestTo)},{"$push":{'Followers':ObjectId(user_id) }})  
                        t2 =db.users.update_one({"_id": ObjectId(user_id)},{"$push":{'Following':ObjectId(SentRequestTo) }}) 
                        if t1.modified_count != 0 and t2.modified_count != 0:
                            return FollowResponse(
                            message="User sent the Follow Request successfully",user_info=UserInfo(
                            id= str(sentto_info['_id']),
                            email=sentto_info['Email'],
                            first_name=sentto_info['FirstName'],
                            last_name=sentto_info['LastName'],
                            age= sentto_info['Age'],
                            account_type=sentto_info['AccountType'],
                            gender=sentto_info['Gender'],
                            )),200

                    raise ProblemException(status=409,title='error',detail='you cannot perform such request to a private account or you  are sending to your self' )
                raise ProblemException(status=404,title='error',detail='no user found') 
                
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def get_all_followers(user_id):  # noqa: E501
    if user_id :
        try: 
            user_info = db.users.find_one({"_id": ObjectId(user_id)},{'AccountType':1})
            if user_info:
                if user_info['AccountType'] == 'public':
                   
                    ListOfFollowers =  db.users.aggregate([
                                        {
                                            '$match': {
                                                '_id': ObjectId('6342c262859f381e72fb371c')
                                            }
                                        }, {
                                            '$lookup': {
                                                'from': 'users', 
                                                'localField': 'Followers', 
                                                'foreignField': '_id', 
                                                'as': 'Followers'
                                            }
                                        }, {
                                            '$project': {
                                                'Followers.Password': 0, 
                                                'Followers.Followers': 0, 
                                                'Followers.Following': 0, 
                                                'Followers.IncomingFollow': 0, 
                                                'Followers.PendingFollow': 0
                                             
                                            }
                                        }
                                    ])
                    Followers= list(ListOfFollowers)[0]['Followers']             
                    for each in Followers:
                        each['_id'] = str(each['_id'])
                    return GetFollowersResponse(message='User get the list of Following  successfully',users=Followers)
                raise ProblemException(status=409,title='error',detail='you cannot perform such request to a  private account' )
            raise ProblemException(status=404,title='error',detail='no user found')    
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def get_all_following(user_id):  # noqa: E501
    if user_id :
        try: 
            user_info = db.users.find_one({"_id": ObjectId(user_id)},{'AccountType':1})
            if user_info:
                if user_info['AccountType'] == 'public':
                   
                    ListOfFollowing =  db.users.aggregate([
                                        {
                                            '$match': {
                                                '_id': ObjectId('6342c262859f381e72fb371c')
                                            }
                                        }, {
                                            '$lookup': {
                                                'from': 'users', 
                                                'localField': 'Following', 
                                                'foreignField': '_id', 
                                                'as': 'Following'
                                            }
                                        }, {
                                            '$project': {
                                                'Following.Password': 0, 
                                                'Following.Followers': 0, 
                                                'Following.Following': 0, 
                                                'Following.IncomingFollow': 0, 
                                                'Following.PendingFollow': 0
                                             
                                            }
                                        }
                                    ])
                    Following = list(ListOfFollowing)[0]['Following']             
                    for each in Following:
                        each['_id'] = str(each['_id'])
                    return GetFollowingResponse(message='User get the list of Following  successfully',users=Following)
                raise ProblemException(status=409,title='error',detail='you cannot perform such request to a  private account' )
            raise ProblemException(status=404,title='error',detail='no user found')    
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def getall():
    try:

        ListOfUsers = db.users.aggregate([{'$match':{}},{ "$project": { "_id": { "$toString": "$_id" } ,'Email':1,'FirstName':1,'LastName':1,"AccountType": 1,"Age": 1 } }])
        if ListOfUsers:
             return GetAllResponse(message='User get the list  users  successfully',users=list(ListOfUsers))
        raise ProblemException(status=404,title='error',detail='no users found')
    except  errors.PyMongoError:
        raise ProblemException(status=500,title='error',detail='internet server error')

def getuser(user_id):  # noqa: E501
    if user_id:
        try:
            user_info = db.users.find_one({"_id": ObjectId(user_id)})
            if user_info:
                user_info['_id']= str(user_info['_id'])
                return GetUserResponse(
                    message="User get the user info  successfully",user_info=UserInfo(
                    id= user_info['_id'],
                    email=user_info['Email'],
                    first_name=user_info['FirstName'],
                    last_name=user_info['LastName'],
                    age= user_info['Age'],
                    account_type=user_info['AccountType'],
                    gender=user_info['Gender'],
                    )),200

            raise ProblemException(status=404,title='error',detail='no user found')  
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def login(email=None,password=None,result=None): 
    if connexion.request.is_json :
        email = connexion.request.get_json()['Email']
        password = connexion.request.get_json()['Password']     
    if email and password :
        try:
            result = db.users.find_one({'Email':email},{'Followers':0,'Following':0,'PendingFollow':0,'IncomingFollow':0})
            if result and  bcrypt.checkpw( password.encode('utf-8'),result['Password']):
                del result['Password']
                result['_id'] = str(result["_id"])
                token = jwt.encode(payload=result,key ='secret', algorithm='HS256')
                istheretoken = db.token.find_one({'user_id':ObjectId(result['_id'])})
                if istheretoken:
                    if ( istheretoken['status']):
                        raise ProblemException(status=409,title='conflict',detail={'message' :'you  are already logged in.','token ':token})
                        
                    else:
                        db.token.update_one({"user_id":ObjectId(result['_id'])},{"$set":{'status':True}})
                else:
                    db.token.insert_one({'user_id':ObjectId(result['_id']),'token':token,'status':True})
                return {'message':'User logged in successfully','token':token,'userinfo':result},200
            raise ProblemException(status=401 ,title='error',detail='Invalid email or password')
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def logout(user_id=None,AddTokenToBlacklist=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    token = connexion.context['token_info']['token']
    user_id = tokenpayload['_id']
    if user_id :
        try:
            tokencheck = db.token.find_one({'token':token})
            if tokencheck:
                if tokencheck['status']:
                    db.token.update_one({"user_id": ObjectId(user_id)},{"$set":{"status":False}})
                    return LogoutResponse(message="User logged out successfully",user_info=UserInfo(
                            id= user_id,
                            email=tokenpayload['Email'],
                            first_name=tokenpayload['FirstName'],
                            last_name=tokenpayload['LastName'],
                            age= tokenpayload['Age'],
                            account_type=tokenpayload['AccountType'],
                            gender=tokenpayload['Gender'],
                        )),200
            raise ProblemException(status=409,title='error',detail='you are already logged out/ no account ')
        except  errors.PyMongoError:
            raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def rejectfollow(user_id=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        follower_ID = connexion.request.get_json()["_id"]
        if follower_ID and user_id:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                follower_info = db.users.find_one({"_id": ObjectId(follower_ID)})
                if follower_info:
                    if user_info['AccountType'] == 'private':                      
                        if  CheckIfexist(follower_ID,user_info['PendingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='you had sent before a follow request')   
                        if CheckIfexist(follower_ID,user_info['Following']) or CheckIfexist(follower_ID,user_info['Followers']):
                            raise  ProblemException(status=409,title='conflict',detail='you already one of his followers/following')
                        if  not CheckIfexist(follower_ID,user_info['IncomingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='the user didnt sent you a follow request')       
                        t1=db.users.update_one({"_id": ObjectId(follower_ID)},{"$pull":{'PendingFollow': ObjectId(user_id)}})  
                        t2 =db.users.update_one({"_id": ObjectId(user_id)},{"$pull":{'IncomingFollow': ObjectId(follower_ID)  }}) 
                        if t1.modified_count != 0 and t2.modified_count != 0:
                                return RejectfollowResponse(
                                    message="User rejected the Follow Request successfully",user_info=UserInfo(
                                    id= str(follower_info['_id']),
                                    email=follower_info['Email'],
                                    first_name=follower_info['FirstName'],
                                    last_name=follower_info['LastName'],
                                    age= follower_info['Age'],
                                    account_type=follower_info['AccountType'],
                                    gender=follower_info['Gender'],
                                    )),200 
                    raise ProblemException(status=409,title='error',detail='you cannot perform such request if your account is  public account' )
                raise ProblemException(status=404,title='error',detail='no user found') 
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
        raise ProblemException(status=400 ,title='error',detail='Bad Request')

def requestfollow( SentRequestTo=None):  # noqa: E501
    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        SentRequestTo = connexion.request.get_json()["_id"]
        if SentRequestTo and user_id:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                sentto_info = db.users.find_one({"_id": ObjectId(SentRequestTo)})
                if sentto_info :
                    if sentto_info['AccountType'] == 'private' and user_info !=SentRequestTo:
                        if user_info['AccountType'] == 'private':                         
                            if  CheckIfexist(SentRequestTo,user_info['IncomingFollow']):
                                raise  ProblemException(status=409,title='conflict',detail='you cannot send follow request if he already sent you a request')    
                        if  CheckIfexist(SentRequestTo,user_info['PendingFollow']):
                            raise  ProblemException(status=409,title='conflict',detail='you have already sent the request ')   
                        if CheckIfexist(SentRequestTo,user_info['Following']) or CheckIfexist(SentRequestTo,user_info['Followers']):
                            raise  ProblemException(status=409,title='conflict',detail='you already one of his followers/following')
                                
                        t1=db.users.update_one({"_id": ObjectId(SentRequestTo)},{"$push":{'IncomingFollow':user_id}})  
                        t2 =db.users.update_one({"_id": ObjectId(user_id)},{"$push":{'PendingFollow':SentRequestTo}}) 
                        if t1.modified_count != 0 and t2.modified_count != 0:
                            return RequestfollowResponse(
                            message="User sent the Follow Request successfully",user_info=UserInfo(
                            id= str(sentto_info['_id']),
                            email=sentto_info['Email'],
                            first_name=sentto_info['FirstName'],
                            last_name=sentto_info['LastName'],
                            age= sentto_info['Age'],
                            account_type=sentto_info['AccountType'],
                            gender=sentto_info['Gender'],
                            )),200
                    raise ProblemException(status=409,title='error',detail='you cannot perform such request to a public account or you  are sending to your self' )
                raise ProblemException(status=404,title='error',detail='no user found') 
                
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def sign_up(InputData=None):  # noqa: E501
    if connexion.request.is_json:
        InputData = connexion.request.get_json()
        if InputData:
            try:
                email_exist = db.users.find_one({'Email':InputData['Email']}) 
                if email_exist:
                    raise ProblemException(status=409,title='error',detail='we have found an existing account using the same email address')
                payload = InputData
                InputData['Password'] =  bcrypt.hashpw(InputData['Password'].encode('utf8'), bcrypt.gensalt())
                InputData['Followers'] =[]
                InputData['Following'] =[]
                InputData['PendingFollow'] =[]
                InputData['IncomingFollow']= []
                result = db.users.insert_one(InputData)
                if result.inserted_id:
                    id = str (result.inserted_id)
                    return SignupResponse(message='User signed up successfully',user_info=UserInfo(
                        id= id,
                        email=InputData['Email'],
                        first_name=InputData['FirstName'],
                        last_name=InputData['LastName'],
                        age= InputData['Age'],
                        account_type=InputData['AccountType'],
                        gender=InputData['Gender'],
                    )),201
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')

def unfollow(user_id=None):  # noqa: E501


    tokenpayload = connexion.context['token_info']['decoded_token']
    user_id = tokenpayload['_id']
    if connexion.request.is_json and user_id:
        SentRequestTo = connexion.request.get_json()["_id"]
        if SentRequestTo and user_id:
            try:
                user_info = db.users.find_one({"_id": ObjectId(user_id)})
                sentto_info = db.users.find_one({"_id": ObjectId(SentRequestTo)})
                if sentto_info and user_info:
                    if not CheckIfexist(SentRequestTo,user_info['Followers']) and   not CheckIfexist(SentRequestTo,user_info['Following']):
                        raise ProblemException(status=409,title='conflict',detail='no follower or following ')
                    t1=db.users.update_one({"_id": ObjectId(SentRequestTo)},{"$pull":{'Followers':ObjectId(user_id) ,'Following':ObjectId(user_id) }})  
                    t2=db.users.update_one({"_id": ObjectId(user_id)},{"$pull":{'Following':ObjectId(SentRequestTo) ,'Followers':ObjectId(SentRequestTo)}})
                    if t1.modified_count != 0 or t2.modified_count != 0:
                        return UnfollowResponse(
                            message="User Unfollowed successfully",user_info=UserInfo(
                            id= str(sentto_info['_id']),
                            email=sentto_info['Email'],
                            first_name=sentto_info['FirstName'],
                            last_name=sentto_info['LastName'],
                            age= sentto_info['Age'],
                            account_type=sentto_info['AccountType'],
                            gender=sentto_info['Gender'],
                            )),200
                raise ProblemException(status=404,title='error',detail='no user found') 
                
            except  errors.PyMongoError:
                raise ProblemException(status=500,title='error',detail='internet server error')
    raise ProblemException(status=400 ,title='error',detail='Bad Request')
