pkgname = "python-flask"
pkgver = "3.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
    "python-wheel",
]
depends = [
    "python-blinker",
    "python-click",
    "python-itsdangerous",
    "python-jinja2",
    "python-werkzeug",
]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Python micro framework for building web applications"
license = "MIT"
url = "https://github.com/pallets/flask"
source = f"https://github.com/pallets/flask/archive/{pkgver}.tar.gz"
sha256 = "80af55cb764cb4d2303ea13877d752a4aa19af898d4e374e0bcdcf1e98fa56e0"


def post_install(self):
    self.install_license("LICENSE.txt")
