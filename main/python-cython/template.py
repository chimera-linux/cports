pkgname = "python-cython"
pkgver = "3.1.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
depends = ["python"]
pkgdesc = "C extensions for Python"
license = "Apache-2.0"
url = "https://cython.org"
source = f"$(PYPI_SITE)/c/cython/cython-{pkgver}.tar.gz"
sha256 = "505ccd413669d5132a53834d792c707974248088c4f60c497deb1b416e366397"
# check: flaky tests
options = ["!check"]
