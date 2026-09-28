pkgname = "yamllint"
pkgver = "1.38.0"
pkgrel = 1
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
sha256 = "09e5f29531daab93366bb061e76019d5e91691ef0a40328f04c927387d1d364d"
