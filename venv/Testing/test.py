import unittest
import testingMain

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = testingMain.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'aman'
        result = testingMain.do_stuff(test_param)
        self.assertTrue(isinstance(result,ValueError))
if __name__ =='__main__':
    unittest.main()