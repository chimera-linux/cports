pkgname = "python-chardet"
pkgver = "6.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Universal encoding detector for Python"
license = "LGPL-2.1-only"
url = "https://github.com/chardet/chardet"
source = f"$(PYPI_SITE)/c/chardet/chardet-{pkgver}.tar.gz"
sha256 = "aaa00ede13dd39a582de2b1254221a1f3e1c77e7738036431b6cb7e6a05b4f19"
# dependency of pytest
options = ["!check"]
