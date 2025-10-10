pkgname = "python-pycurl"
pkgver = "7.45.7"
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
license = "LGPL-2.0-or-later AND MIT"
url = "http://pycurl.io"
source = f"$(PYPI_SITE)/p/pycurl/pycurl-{pkgver}.tar.gz"
sha256 = "9d43013002eab2fd6d0dcc671cd1e9149e2fc1c56d5e796fad94d076d6cb69ef"


def post_install(self):
    for f in self.cwd.glob("COPYING-*"):
        self.install_license(f)
