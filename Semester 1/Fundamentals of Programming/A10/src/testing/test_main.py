import unittest

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover("", "test*.py")
    unittest.TextTestRunner().run(suite)
