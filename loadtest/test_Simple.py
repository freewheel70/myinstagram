import unittest
import time
from funkload.FunkLoadTestCase import FunkLoadTestCase
from funkload.utils import Data
from webunit.utility import Upload


class Simple(FunkLoadTestCase):
    """This test use a configuration file Simple.conf."""

    def setUp(self):
        """Setting up test."""
        self.server_url = self.conf_get('main', 'url')

        # def test_simple(self):
        #     # The description should be set in the configuration file
        #     server_url = self.server_url
        #     # begin test ---------------------------------------------
        #     nb_time = self.conf_getInt('test_simple', 'nb_time')
        #     for i in range(nb_time):
        #         self.get(server_url, description='Get URL')
        #         # end test -----------------------------------------------

        # def test_funkload(self):
        #     login_url = self.conf_get('test_freewheel', 'login_url')
        #     response = self.post(login_url,
        #                              params=[
        #                                  ["email","lizhihong370@gmail.com"],
        #                                  ["password","ierg4080"]
        #                              ],
        #                              description="Login as lzh")
        #     self.assertEqual(response.code, 200)
        #     self.assertEqual(response.body, "hello world")

        # response = self.post("https://secure.s3.ierg4210.ie.cuhk.edu.hk/funkload.php",
        #                      params=[
        #                          ["email", "lizhihong370@gmail.com"],
        #                          ["password", "ierg4080"]
        #                      ],
        #                      description="Login as lzh")
        # self.assertEqual(response.code, 200)
        # self.assertEqual(response.body, "hello world")

    def test_freewheel(self):
        search_url=self.conf_get('test_freewheel', 'search_url')
        response = self.post(search_url,
                             params=[
                                 ["key", "madao"]
                             ],
                             description="Search keyword")

        # self.assertEqual(response.body, "hello world")
        #
        # main_url = self.conf_get('test_freewheel', 'main_url')
        # logout_url = self.conf_get('test_freewheel', 'logout_url')
        # upload_url = self.conf_get('test_freewheel', 'upload_url')
        # profile_url = self.conf_get('test_freewheel', 'profile_url')
        # login_url = self.conf_get('test_freewheel', 'login_url')
        # signup_url= self.conf_get('test_freewheel', 'signup_url')
        # lobby_url = self.conf_get('test_freewheel', 'lobby_url')
        # one_friend = self.conf_get('test_freewheel', 'one_friend')
        #
        # # Get homepage
        # self.get(main_url, description='Visit homepage')
        #
        # username = "testuser"+time.strftime("%Y%m%d_%H%M%S", time.gmtime())
        # email=username+"@gmail.com"
        # password="ierg4080"
        #
        # # register
        # response = self.post(signup_url,
        #                      params=[
        #                          ["username",username],
        #                          ["email", email],
        #                          ["password", password]
        #                      ],
        #                      description="Register a new account")
        #
        # # login :
        # response = self.post(login_url,
        #                      params=[
        #                          ["email", email],
        #                          ["password", password]
        #                      ],
        #                      description="Login")
        #
        # # self.assertEqual(response.body, "hello world")
        #
        # # need to save cookie ?
        #
        # # View profile
        # response = self.get(profile_url, description='Visit profile page')
        #
        # # upload a file
        # response = self.post(upload_url,
        #                      params=[['image', Upload('ginsang.jpg')],
        #                              ['description', 'ginsang666']],
        #                      description="Upload a new image")
        # # self.assertEqual(response.body, "hello world")
        #
        # # view Lobby
        # response = self.get(lobby_url, description='Visit lobby page')
        #
        #
        # # view one friend
        # response = self.get(one_friend, description='View a friend profile page')
        #
        #
        # # View profile
        # response = self.get(profile_url, description='View profile page')
        #
        #
        # # log out
        # response = self.get(logout_url, description='Logout')



if __name__ in ('main', '__main__'):
    unittest.main()
