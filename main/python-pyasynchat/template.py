pkgname = "python-pyasynchat"
pkgver = "1.0.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-pyasyncore"]
checkdepends = [
    "python-pytest",
    "python-tests",
    *depends,
]
pkgdesc = "Python asynchat for 3.12"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Python-2.0"
url = "https://github.com/simonrob/pyasynchat"
source = f"$(PYPI_SITE)/p/pyasynchat/pyasynchat-{pkgver}.tar.gz"
sha256 = "3f5333df649e46c56d48c57e6a4b7163fd07f626bfd884e22ef373ab3c3a4670"
