import db_process
import unittest
import os

class TestReadFile(unittest.TestCase):
    def testFindFile(self):
        test_path = "static"
        answer = [os.path.join(test_path, "test.pickle")]
        self.assertEqual(db_process.read_files(test_path), answer)

    def testNotFindFolder(self):
        test_path = "static2"
        answer = [os.path.join(test_path, "test.pickle")]
        self.assertEqual(db_process.read_files(test_path), None)

    def testNotFindFolderButNoPickle(self):
        test_path = ".venv"
        answer = [os.path.join(test_path, "test.pickle")]
        self.assertEqual(db_process.read_files(test_path), None)


if __name__ == "__main__":
    unittest.main()