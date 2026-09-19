pkgname = "python-time-machine"
pkgver = "3.5.1"
pkgrel = 0
build_style = "python_pep517"
# pytester plugin needed for the 'testdir' fixture (pytest 8.4 doesn't
# enable it)
# fuzz tests rely on TZ being interpreted as a zoneinfo filename, which
# musl's tzset mis-parses for legacy zone names like GB-Eire/EST5EDT
make_check_args = [
    "-p",
    "pytester",
    "--deselect",
    "tests/test_fuzz.py::test_localtime_and_gmtime_match_datetime",
    "--deselect",
    "tests/test_fuzz.py::test_naive_datetime_modes",
]
hostmakedepends = [
    "python-build",
    "python-devel",
    "python-installer",
    "python-setuptools",
]
depends = ["python-dateutil", "python-tokenize-rt"]
checkdepends = [
    "python-freezegun",
    "python-hypothesis",
    "python-pytest",
    *depends,
]
pkgdesc = "Python library for mocking the current time"
license = "MIT"
url = "https://github.com/adamchainz/time-machine"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "409d04bd59a3b2cc79f232968e1902a35daa3d1b4310952ab8682d852ac074ab"


def post_install(self):
    self.install_license("LICENSE")
