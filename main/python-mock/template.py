pkgname = "python-mock"
pkgver = "5.2.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python"]
checkdepends = ["python-pytest"]
pkgdesc = "Python mock library"
license = "BSD-2-Clause"
url = "https://mock.readthedocs.org"
source = f"$(PYPI_SITE)/m/mock/mock-{pkgver}.tar.gz"
sha256 = "4e460e818629b4b173f32d08bf30d3af8123afbb8e04bb5707a1fd4799e503f0"


def post_install(self):
    self.install_license("LICENSE.txt")
