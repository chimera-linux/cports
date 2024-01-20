pkgname = "python-flask"
pkgver = "3.0.1"
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
sha256 = "f6a65bf1edb37df61ac14796fd32a0a31b0888b3396e2fd22bb6f64751bd8ccc"


def post_install(self):
    self.install_license("LICENSE.rst")
