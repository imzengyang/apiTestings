import unittest
import requests

from ddt import ddt, data, unpack


from library.getData import get_xls_data



@ddt
class APItesting(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        pass

    @data(*get_xls_data('./data/user.xls'))
    @unpack
    def test_post(self,tocken,title,tab,content,code):
        url = 'http://118.31.19.120:3000/api/v1/topics'

        jsondata = {
            "accesstoken": tocken,
            "title": title,
            "tab": tab,
            "content": content
        }
        res = requests.post(url,json=jsondata)
        assert res.status_code == code
        

    @classmethod
    def tearDownClass(self):
        pass
