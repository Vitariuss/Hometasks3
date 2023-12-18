import yaml
from sshcheckers import ssh_checkout_negative

with open('config.yaml') as f:
    testdata = yaml.safe_load(f)


class TestNegative:

    def test_step1(self, make_bad_arx):
        # test1 ( take docs from folder: out and copy these docs to folder1)
        assert ssh_checkout_negative("0.0.0.0", "user2", "1234",
                                     "cd {}; 7z e bad_arx.{} -o{} -y".format(testdata["folder_out"], testdata["type"],
                                                                             testdata["folder_ext1"]),
                                     text="ERROR"), "Test1 FAIL"

    def test_step2(self):
        # test2 (show info about arx2.7z)
        assert ssh_checkout_negative("0.0.0.0", "user2", "1234",
                                     "cd {}; 7z t bad_arx.{}".format(testdata["folder_out"], testdata["type"]),
                                     text="ERROR"), "Test2 FAIL"
