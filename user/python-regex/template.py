pkgname = "python-regex"
pkgver = "2026.7.19"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
makedepends = ["python-devel"]
checkdepends = ["python-pytest"]
pkgdesc = "Extended regex module for Python"
license = "Apache-2.0"
url = "https://github.com/mrabarnett/mrab-regex"
source = f"$(PYPI_SITE)/r/regex/regex-{pkgver}.tar.gz"
sha256 = "7e77b324909c1617cbb4c668677e2c6ae13f44d7c1de0d4f15f2e3c10f3315b5"
# can't import the native lib? works when installed
options = ["!check"]
