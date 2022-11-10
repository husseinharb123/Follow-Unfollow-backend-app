# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

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
from openapi_server.test import BaseTestCase


class TestUserController(BaseTestCase):
    """UserController integration test stubs"""

    def test_approvefollow(self):
        """Test case for approvefollow

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/approvefollow',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cancel_request(self):
        """Test case for cancel_request

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/CancelRequest',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_account(self):
        """Test case for delete_account

        
        """
        body = None
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/DeleteAccount',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_follow(self):
        """Test case for follow

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/follow',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_followers(self):
        """Test case for get_all_followers

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/{user_id}/followers'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_following(self):
        """Test case for get_all_following

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/{user_id}/following'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getall(self):
        """Test case for getall

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/getall',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_getuser(self):
        """Test case for getuser

        
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/{user_id}'.format(user_id='user_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login(self):
        """Test case for login

        
        """
        login_request = openapi_server.LoginRequest()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/login',
            method='POST',
            headers=headers,
            data=json.dumps(login_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout(self):
        """Test case for logout

        
        """
        body = None
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/logout',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_rejectfollow(self):
        """Test case for rejectfollow

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/Rejectfollow',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_requestfollow(self):
        """Test case for requestfollow

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/requestfollow',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_sign_up(self):
        """Test case for sign_up

        
        """
        user_info = {
  "Email" : "Email",
  "FirstName" : "FirstName",
  "_id" : "_id",
  "LastName" : "LastName",
  "Gender" : "male",
  "AccountType" : "private",
  "Age" : 18,
  "Password" : "Password"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/signup',
            method='POST',
            headers=headers,
            data=json.dumps(user_info),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unfollow(self):
        """Test case for unfollow

        
        """
        user_id = openapi_server.UserId()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/unfollow',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
