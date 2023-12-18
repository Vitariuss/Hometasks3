import pytest
import yaml
import random
import string
from datetime import datetime
from sshcheckers import ssh_checkout, upload_files, ssh_getout

with open('config.yaml') as file:
    testdata = yaml.safe_load(file)


@pytest.fixture(autouse=True, scope="module")
def deploy():
    res = []
    upload_files("0.0.0.0", "user2", "1234", "/home/user/p7zip-full.deb",
                 "/home/user2/p7zip-full.deb")
    res.append(
        ssh_checkout("0.0.0.0", "user2", "1234", "echo '1234' | sudo -S dpkg -i p7zip-full.deb",
                     "Настраивается пакет"))
    res.append(ssh_checkout("0.0.0.0", "user2", "1234", "echo '1234' | sudo -S dpkg -s p7zip-full",
                            "Status: install ok installed"))
    return all(res)


@pytest.fixture(autouse=True, scope="module")
def make_folders():
    return ssh_checkout("0.0.0.0", "user2", "1234",
                        "mkdir {} {} {} {}".format(
                            testdata["folder_in"], testdata["folder_out"], testdata["folder_ext1"],
                            testdata["folder_ext2"]),
                        "")


@pytest.fixture(autouse=True, scope="module")
def make_log():
    return ssh_checkout("0.0.0.0", "user2", "1234",
                        "touch {}".format(
                            testdata["folder_in"]),
                        "")


@pytest.fixture(autouse=True, scope="class")
def make_files():
    list_of_files = []
    for i in range(testdata["count"]):
        filename = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout("0.0.0.0", "user2", "1234",
                        "cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(testdata["folder_in"],
                                                                                               filename,
                                                                                               testdata["bs"]), ""):
            list_of_files.append(filename)
    return list_of_files


@pytest.fixture(autouse=True, scope="module")
def clear_folders():
    return ssh_checkout("0.0.0.0", "user2", "1234",
                        "rm -rf {}/* {}/* {}/* {}/*".format(testdata["folder_in"], testdata["folder_out"],
                                                            testdata["folder_ext1"],
                                                            testdata["folder_ext2"]),
                        "")


@pytest.fixture()
def make_bad_arx():
    ssh_checkout("0.0.0.0", "user", "1234",
                 "cd {}; 7z a {}/bad_arx".format(testdata["folder_in"], testdata["folder_out"]),
                 "Everything is Ok")
    ssh_checkout("0.0.0.0", "user2", "1234",
                 "truncate -s 1 {}/bad_arx.{}".format(testdata["folder_out"], testdata["type"]),
                 "")


@pytest.fixture(autouse=True)
def log_test():
    fileavg = open("/proc/loadavg")
    with open("/tmp/stat.txt", "a") as file_object:
        file_object.write(datetime.now().strftime("%H:%M:%S.%f") + ", " + str(testdata["count"]) + ", " + testdata[
            "bs"] + ", " + fileavg.read())


@pytest.fixture()
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield print("Stop: {}".format(datetime.now().strftime("%H:%M:%S.%f")))


@pytest.fixture(autouse=True)
def stat(request):
    time = datetime.now().strftime("%H:%M:%S.%f")
    name = request.node.name
    with open("stat.txt", "a", encoding="utf-8") as f, open("/proc/loadavg", "r", encoding="utf-8") as fr:
        f.write(
            f'{name}\ntime start: {time}\ncount = {testdata["count"]}, \
            size = {testdata["bs"]}\nCPU load: {fr.readlines()[-1]}\n')


@pytest.fixture(autouse=True, scope="module")
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")


@pytest.fixture(scope="module")
def safe_log(starttime):
    with open(stat.txt, "w") as f:
        f.write(ssh_getout("0.0.0.0", "user", "1234", "journalctl --since {}".format(starttime())))
