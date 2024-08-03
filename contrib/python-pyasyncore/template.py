pkgname = "python-pyasyncore"
pkgver = "1.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = [
    "python-pytest",
    "python-tests",
]
pkgdesc = "Python asyncore for 3.12"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/simonrob/pyasyncore"
source = f"$(PYPI_SITE)/p/pyasyncore/pyasyncore-{pkgver}.tar.gz"
sha256 = "2c7a8b9b750ba6260f1e5a061456d61320a80579c6a43d42183417da89c7d5d6"
# relies on <3.12 unittest imports
options = ["!check"]
