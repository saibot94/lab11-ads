import unittest

if __name__ == '__main__':
    testSuite = unittest.TestLoader().discover('.', pattern="*_Test.py")
    unittest.TextTestRunner().run(testSuite)

