pkgname = "python-pylint"
pkgver = "3.3.7"
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
    "python-isort",
    "python-mccabe",
    "python-platformdirs",
    "python-tomlkit",
]
checkdepends = [
    *depends,
    "python-pytest",
    "python-pytest-benchmark",
]
pkgdesc = "Python code static checker"
license = "GPL-2.0-or-later"
url = "https://github.com/pylint-dev/pylint"
source = f"$(PYPI_SITE)/p/pylint/pylint-{pkgver}.tar.gz"
sha256 = "2b11de8bde49f9c5059452e0c310c079c746a0a8eeaa789e5aa966ecc23e4559"
# FIXME: failing tests
options = ["!check"]
