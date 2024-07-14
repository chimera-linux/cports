pkgname = "python-flask"
pkgver = "3.0.3"
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
sha256 = "d4d25a9b939b5e0e14b3dbc118805101a01eff0b47b1456b4a775a568af2ecd6"


def post_install(self):
    self.install_license("LICENSE.txt")
