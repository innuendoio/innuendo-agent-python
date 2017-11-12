import unittest, os

TEST_PATTERN = 'test*'
CURRENT_DIR = os.path.dirname(__file__)

def load_tests(loader, standard_tests, pattern):
    # top level directory cached on loader instance
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    standard_tests.addTests(package_tests)
    return standard_tests

def suite():
    global CURRENT_DIR, TEST_PATTERN

    # Inits the loader and suite
    loader = unittest.TestLoader()
    suite  = unittest.TestSuite()

    current_dir = os.path.dirname(__file__)

    # Discovers all the tests
    tests = loader.discover(start_dir=CURRENT_DIR, pattern=TEST_PATTERN)

    # Adds all the tests found
    suite.addTests(tests)

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())