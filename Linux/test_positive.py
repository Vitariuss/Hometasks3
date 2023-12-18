import subprocess
import yaml
from sshcheckers import ssh_checkout

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)

    # Preparation of a directory


class TestPositive:

    def test_step1(self, make_bad_arx):
        # test1 (create archive)
        result1 = ssh_checkout("0.0.0.0", "user2", "1234",
                               "cd {}; 7z a -t{} {}/arx2".format(testdata["folder_in"], testdata["type"],
                                                                 testdata["folder_out"]),
                               "Everything is Ok")
        # check if arx2.7z in out
        result2 = ssh_checkout("0.0.0.0", "user2", "1234", "cd {}; ls".format(testdata["folder_out"]),
                               "arx2.{}".format(testdata["type"]))
        assert result1 and result2, "Test1 FAIL"

    def test_step2(self, make_files):
        # test1 (take docs from folder: out and copy these docs to folder1)
        result1 = ssh_checkout("0.0.0.0", "user2", "1234",
                               "cd {}; 7z e arx2.{} -o{} -y".format(testdata["folder_out"], testdata["type"],
                                                                    testdata["folder_ext1"]),
                               "Everything is Ok")
        result2 = ssh_checkout("0.0.0.0", "user2", "1234", "cd {}; ls".format(testdata["folder_ext1"]), make_files[0])
        assert result1 and result2, "Test2 FAIL"

    def test_step3(self):
        # test3 (show info about arx2.7z)
        assert ssh_checkout("0.0.0.0", "user2", "1234",
                            "cd {}; 7z t arx2.{}".format(testdata["folder_out"], testdata["type"]),
                            "Everything is Ok"), "Test3 FAIL"

    def test_step3_1(self):
        # test3 (show info about arx2.7z)
        assert ssh_checkout("0.0.0.0", "user2", "1234",
                            "cd {}; 7z l arx2.{}".format(testdata["folder_out"], testdata["type"]),
                            "Name"), "Test3_1 FAIL"

    def test_step4(self):
        # test4 (add archive update)
        assert ssh_checkout("0.0.0.0", "user2", "1234",
                            "cd {}; 7z u {}/arx2.{}".format(testdata["folder_in"], testdata["folder_out"],
                                                            testdata["type"]),
                            "Everything is Ok"), "Test4 FAIL"

    def test_step5(self):
        # test5 (delete docs one and two from archive in folder out)
        assert ssh_checkout("0.0.0.0", "user2", "1234",
                            "cd {}; 7z d arx2.{}".format(testdata["folder_out"], testdata["type"]),
                            "Everything is Ok"), "Test5 FAIL"

    def test_step6(self):
        # test6 (check crc32)
        res = subprocess.run("crc32 /home/user/out/arx2.7z", shell=True, stdout=subprocess.PIPE, encoding='utf-8')
        assert ssh_checkout("0.0.0.0", "user2", "1234",
                            "cd {}; 7z h arx2.{}".format(testdata["folder_out"], testdata["type"]),
                            res.stdout.rstrip().upper()), "test6 FAIL"
