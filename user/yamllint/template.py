pkgname = "yamllint"
pkgver = "1.35.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = [
    "python-pathspec",
    "python-pyyaml",
]
checkdepends = [
    "musl-locales",
    "python-pytest",
    *depends,
]
pkgdesc = "Linter for YAML files"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-or-later"
url = "https://yamllint.readthedocs.io"
source = f"$(PYPI_SITE)/y/yamllint/yamllint-{pkgver}.tar.gz"
sha256 = "7a003809f88324fd2c877734f2d575ee7881dd9043360657cc8049c809eba6cd"
