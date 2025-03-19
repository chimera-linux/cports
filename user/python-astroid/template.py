pkgname = "python-astroid"
pkgver = "3.3.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
checkdepends = [
    "python-pytest",
    "python-mypy",
]
pkgdesc = "Abstract syntax tree for Python with inference support"
license = "LGPL-2.1-or-later"
url = "https://github.com/pylint-dev/astroid"
source = f"$(PYPI_SITE)/a/astroid/astroid-{pkgver}.tar.gz"
sha256 = "622cc8e3048684aa42c820d9d218978021c3c3d174fb03a9f0d615921744f550"
