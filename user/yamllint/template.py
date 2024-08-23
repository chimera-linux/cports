pkgname = "yamllint"
pkgver = "1.37.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = [
    "python-pathspec",
    "python-pyyaml",
]
checkdepends = [
    "python-pytest",
    *depends,
]
pkgdesc = "Linter for YAML files"
license = "GPL-3.0-or-later"
url = "https://yamllint.readthedocs.io"
source = f"$(PYPI_SITE)/y/yamllint/yamllint-{pkgver}.tar.gz"
sha256 = "81f7c0c5559becc8049470d86046b36e96113637bcbe4753ecef06977c00245d"
