pkgname = "python-outcome"
pkgver = "1.3.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-attrs"]
checkdepends = ["python-pytest", *depends]
pkgdesc = "Capture the outcome of Python calls"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/python-trio/outcome"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5427e7d3c48bcb9d383e08ba057359b570c6118d0e640da5baeb0e298502a4b2"


def post_install(self):
    self.install_license("LICENSE.MIT")
