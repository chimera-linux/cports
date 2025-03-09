pkgname = "python-pylint"
pkgver = "3.3.5"
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
sha256 = "38d0f784644ed493d91f76b5333a0e370a1c1bc97c22068a77523b4bf1e82c31"
