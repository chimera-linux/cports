pkgname = "python-flask"
pkgver = "3.0.2"
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
checkdepends = ["python-pytest"] + depends
pkgdesc = "Python micro framework for building web applications"
maintainer = "firefly-cpp <iztok@iztok.space>"
license = "MIT"
url = "https://github.com/pallets/flask"
source = f"https://github.com/pallets/flask/archive/{pkgver}.tar.gz"
sha256 = "48843a02c216f7386163b76e9b0d7226716bfbd5155a127cf00ae2094c6c2f16"


def post_install(self):
    self.install_license("LICENSE.rst")
