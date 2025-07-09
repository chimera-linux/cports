pkgname = "python-pycurl"
pkgver = "7.45.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["curl-devel", "openssl3-devel", "python-devel"]
checkdepends = ["python-flask", "python-flaky", "python-pytest"]
pkgdesc = "Python3 interface to libcurl"
license = "MIT"
url = "http://pycurl.io"
source = f"$(PYPI_SITE)/p/pycurl/pycurl-{pkgver}.tar.gz"
sha256 = "2b73e66b22719ea48ac08a93fc88e57ef36d46d03cb09d972063c9aa86bb74e6"


def post_install(self):
    for f in self.cwd.glob("COPYING-*"):
        self.install_license(f)
