pkgname = "python-tornado"
pkgver = "6.5.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python web framework and asynchronous networking library"
license = "Apache-2.0"
url = "https://github.com/tornadoweb/tornado"
source = f"$(PYPI_SITE)/t/tornado/tornado-{pkgver}.tar.gz"
sha256 = "84ceece391e8eb9b2b95578db65e920d2a61070260594819589609ba9bc6308c"
