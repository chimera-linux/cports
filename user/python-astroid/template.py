pkgname = "python-astroid"
pkgver = "3.3.10"
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
sha256 = "c332157953060c6deb9caa57303ae0d20b0fbdb2e59b4a4f2a6ba49d0a7961ce"
