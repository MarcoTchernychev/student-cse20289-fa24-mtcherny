#Marco Tchernychev
#mtcherny@nd.edu
import unittest
import hw6searchsrc
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/tests/data/"
class TestClass(unittest.TestCase):
    def test_loc(self):
        self.assertEqual(len(hw6searchsrc.readFile(path+"fmnc_manager.cc")), 2310)
    def test_path(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[0], path)
    def test_filename(self):
        self.assertEqual(hw6searchsrc.get_path_and_name(path+"fmnc_manager.cc")[1],"fmnc_manager.cc")

if __name__ == "__main__":
    unittest.main()