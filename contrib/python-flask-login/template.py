pkgname = "python-flask-login"
pkgver = "0.6.3"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # need updating for werkzeug3
    "--deselect=tests/test_login.py::LoginTestCase",
    "--deselect=tests/test_login.py::UnicodeCookieUserIDTestCase",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-flask",
    "python-werkzeug",
]
checkdepends = [
    "python-asgiref",
    "python-blinker",
    "python-pytest",
    "python-semantic_version",
] + depends
pkgdesc = "Flask user session management"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/maxcountryman/flask-login"
source = f"https://github.com/maxcountryman/flask-login/archive/{pkgver}.tar.gz"
sha256 = "3b2489f46d854b5f1d7a55007271d2eae9f744e0935ca7b88ab584c770a7e4d2"


def post_install(self):
    self.install_license("LICENSE")
