pkgname = "python-cppy"
pkgver = "1.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-setuptools_scm",
]
depends = [
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
]
pkgdesc = "Helper for writing Python extensions in C++"
license = "BSD-3-Clause"
url = "https://cppy.readthedocs.io"
source = f"$(PYPI_SITE)/c/cppy/cppy-{pkgver}.tar.gz"
sha256 = "55b5307c11874f242ea135396f398cb67a5bbde4fab3e3c3294ea5fce43a6d68"


def post_install(self):
    self.install_license("LICENSE")
