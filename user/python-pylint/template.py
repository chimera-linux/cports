pkgname = "python-pylint"
pkgver = "3.3.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = [
    "python-astroid",
    "python-dill",
    "python-mccabe",
    "python-isort",
    "python-platformdirs",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python code static checker"
license = "GPL-2.0-or-later"
url = "https://github.com/pylint-dev/pylint"
source = f"$(PYPI_SITE)/p/pylint/pylint-{pkgver}.tar.gz"
sha256 = "b634a041aac33706d56a0d217e6587228c66427e20ec21a019bc4cdee48c040a"
# FIXME: failing tests
options = ["!check"]
