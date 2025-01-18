pkgname = "python-loguru"
pkgver = "0.7.2"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-flit_core",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = [
    "python-colorama",
    "python-freezegun",
    "python-pytest",
    "python-mypy",
]
pkgdesc = "Python logging library"
maintainer = "supermikea <mikewiegmanavila@keemail.me>"
license = "MIT"
url = "https://github.com/Delgan/loguru"
source = f"$(PYPI_SITE)/l/loguru/loguru-{pkgver}.tar.gz"
sha256 = "e671a53522515f34fd406340ee968cb9ecafbc4b36c679da03c18fd8d0bd51ac"


def post_install(self):
    self.install_license("LICENSE")
