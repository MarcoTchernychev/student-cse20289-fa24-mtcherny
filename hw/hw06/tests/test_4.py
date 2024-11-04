#Marco Tchernychev
#mtcherny@nd.edu
import unittest
import hw6searchdir
import subprocess
import os
path = "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/hw06/ex-tests/"
class TestClass(unittest.TestCase):
    
    def test_nrd1(self): #testing nrd-1
        result = subprocess.run(["python3", "hw6searchdir.py", path+"nrd-1/"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"nrd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF\n"
                                    +path+"nrd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF\n"
                                    +path+"nrd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF\n"
                                    +path+"nrd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF\n"
                                    +path+"nrd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 35 OLF\n")
    def test_nrd2(self): #testing nrd-2
        result = subprocess.run(["python3", "hw6searchdir.py", path+"nrd-2/"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"nrd-2/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF\n"
                                    +path+"nrd-2/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF\n"
                                    +path+"nrd-2/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF\n"
                                    +path+"nrd-2/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF\n"
                                    +path+"nrd-2/, TWiCE_Gateway.cc, 991 LOC, 7 I, 6 LI, 22 MF, 5 OLF\n"
                                    +path+"nrd-2/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF\n"
                                    +path+"nrd-2/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 35 OLF\n"
                                    +path+"nrd-2/, fmnc_test_sequence.cc, 2662 LOC, 9 I, 5 LI, 84 MF, 44 OLF\n"
                                    +path+"nrd-2/, ip-utils.cc, 1239 LOC, 5 I, 1 LI, 0 MF, 0 OLF\n"
                                    +path+"nrd-2/, whirlwind_gateway.cc, 1186 LOC, 12 I, 10 LI, 27 MF, 5 OLF\n")
    def test_nrd3(self): #testing nrd-3
        result = subprocess.run(["python3", "hw6searchdir.py", path+"nrd-3/"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"nrd-3/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF\n"
                                    +path+"nrd-3/, AdapterFile.cc, 812 LOC, 9 I, 8 LI, 32 MF, 16 OLF\n"
                                    +path+"nrd-3/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF\n")
    def test_rd1(self): #testing rd-1
        result = subprocess.run(["python3", "hw6searchdir.py", path+"rd-1/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"rd-1/, ParamDictionary.cc, 379 LOC, 3 I, 1 LI, 26 MF, 10 OLF\n"
                                    +path+"rd-1/, PktQueue.cc, 42 LOC, 1 I, 1 LI, 4 MF, 4 OLF\n"
                                    +path+"rd-1/, RIPPS_PktPair.cc, 607 LOC, 5 I, 3 LI, 50 MF, 23 OLF\n"
                                    +path+"rd-1/, Thread_IO.cc, 149 LOC, 7 I, 5 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-1/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 35 OLF\n"
                                    +path+"rd-1/sd/, TWiCE_Gateway.cc, 991 LOC, 7 I, 6 LI, 22 MF, 5 OLF\n"
                                    +path+"rd-1/sd/, whirlwind_gateway.cc, 1186 LOC, 12 I, 10 LI, 27 MF, 5 OLF\n")
    def test_rd2(self): #testing rd-2
        result = subprocess.run(["python3", "hw6searchdir.py", path+"rd-2/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path + "rd-2/, fmnc_client.cc, 10 LOC, 0 I, 0 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-2/, fmnc_connection.cc, 685 LOC, 3 I, 2 LI, 66 MF, 47 OLF\n"
                                    +path+"rd-2/, fmnc_connection_tcp_slice.cc, 609 LOC, 4 I, 3 LI, 43 MF, 24 OLF\n"
                                    +path+"rd-2/, fmnc_manager.cc, 2310 LOC, 18 I, 11 LI, 77 MF, 35 OLF\n"
                                    +path+"rd-2/, fmnc_measurement_packet.cc, 847 LOC, 4 I, 2 LI, 75 MF, 31 OLF\n"
                                    +path+"rd-2/sd2/, fmnc_session.cc, 10 LOC, 0 I, 0 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-2/sd2/, fmnc_support.cc, 26 LOC, 2 I, 2 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-2/sd2/, fmnc_test_analysis.cc, 567 LOC, 7 I, 5 LI, 29 MF, 13 OLF\n"
                                    +path+"rd-2/sd2/, fmnc_test_sequence.cc, 2662 LOC, 9 I, 5 LI, 84 MF, 44 OLF\n"
                                    +path+"rd-2/sd3/, MemPoolCustom.cc, 52 LOC, 2 I, 2 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-2/sd3/, MemPoolObject.cc, 189 LOC, 13 I, 13 LI, 13 MF, 9 OLF\n")
    def test_rd3(self): #testing rd-3
        result = subprocess.run(["python3", "hw6searchdir.py", path+"rd-3/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"rd-3/, Adapter.cc, 724 LOC, 12 I, 11 LI, 42 MF, 16 OLF\n"
                                    +path+"rd-3/, AdapterFile.cc, 812 LOC, 9 I, 8 LI, 32 MF, 16 OLF\n"
                                    +path+"rd-3/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF\n"
                                    +path+"rd-3/mon/, Monitor.cc, 224 LOC, 8 I, 7 LI, 14 MF, 5 OLF\n"
                                    +path+"rd-3/mon/, Thread_Archive.cc, 209 LOC, 5 I, 5 LI, 16 MF, 6 OLF\n"
                                    +path+"rd-3/mon/, Thread_Timer.cc, 588 LOC, 8 I, 6 LI, 36 MF, 17 OLF\n"
                                    +path+"rd-3/packetcache/, PacketCacheEntry.cc, 17 LOC, 2 I, 1 LI, 2 MF, 0 OLF\n"
                                    +path+"rd-3/packetcache/, PacketCacheModule.cc, 137 LOC, 8 I, 5 LI, 7 MF, 3 OLF\n"
                                    +path+"rd-3/packetcache/, PacketCacheSupport.cc, 15 LOC, 2 I, 2 LI, 0 MF, 0 OLF\n"
                                    +path+"rd-3/packetcache/, PacketCacheTable.cc, 610 LOC, 7 I, 5 LI, 7 MF, 4 OLF\n"
                                    +path+"rd-3/packetcache/address/, NetAddress.cc, 291 LOC, 4 I, 3 LI, 30 MF, 16 OLF\n"
                                    +path+"rd-3/packetcache/address/, NetAddressEthernet.cc, 156 LOC, 6 I, 4 LI, 8 MF, 2 OLF\n"
                                    +path+"rd-3/packetcache/address/, NetAddressIPv4.cc, 196 LOC, 6 I, 4 LI, 10 MF, 2 OLF\n"
                                    +path+"rd-3/packetcache/address/, NetAddressIPv4Subnet.cc, 161 LOC, 6 I, 4 LI, 9 MF, 2 OLF\n" )
    def test_rd4(self): #testing rd-4
        result = subprocess.run(["python3", "hw6searchdir.py", path+"rd-4/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"rd-4/, AdapterPCap.cc, 211 LOC, 7 I, 6 LI, 14 MF, 8 OLF\n")
    def test_personal1(self): #testing my first personal nested drrectory
        result = subprocess.run(["python3", "hw6searchdir.py", path+"personal1/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, path+"personal1/p1nest1/p1nest2/p1nest3/, myfile.cc, 0 LOC, 0 I, 0 LI, 0 MF, 0 OLF\n")
    def test_personal2(self): #testing my second personal nested directory
        result = subprocess.run(["python3", "hw6searchdir.py", path+"personal2/", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, "Directory does not exist or lacks source files\n")
    def test_baddir(self): #testing a bad dir
        result = subprocess.run(["python3", "hw6searchdir.py", "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/h06/ex-tests/rd-4", "-r"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        self.assertEqual(result, "Directory does not exist or lacks source files\n")
    def test_bad(self): #testing a bad arg
        result = subprocess.run(["python3", "hw6searchdir.py", "/escnfs/home/mtcherny/repos/student-cse20289-fa24-mtcherny/hw/h06/ex-tests/rd-4", "-r", "--blah"], stdout = subprocess.PIPE, stderr=subprocess.PIPE).stderr.decode('utf-8')
        self.assertTrue("unrecognized arguments" in result)

if __name__ == "__main__":
    unittest.main()