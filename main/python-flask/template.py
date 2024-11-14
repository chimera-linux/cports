pkgname = "python-flask"
pkgver = "3.1.0"
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
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pallets/flask"
source = f"https://github.com/pallets/flask/archive/{pkgver}.tar.gz"
sha256 = "2b362a35e92c72df6da86b4ca2fdc2bc86d667a79e8a1791dc5bda97f5cbb060"


def post_install(self):
    self.install_license("LICENSE.txt")
