import unittest

class EdadError(Exception):
    pass

def func():
    raise EdadError ("Veamos si funciona")

class ExampleTest(unittest.TestCase):
    def test_error(self):
        with self.assertRaises(EdadError):
            func()

if __name__=="__main__":
    unittest.main()



