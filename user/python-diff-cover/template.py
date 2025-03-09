pkgname = "python-diff-cover"
pkgver = "9.3.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-jinja2",
    "python-pygments",
    "python-pluggy",
    "python-chardet",
]
checkdepends = [
    *depends,
    "python-pytest",
    "python-pytest-datadir-nng",
    "python-pytest-mock",
    "python-flake8",
    "python-pylint",
]
pkgdesc = "Automatically find diff lines that need test coverage"
license = "Apache-2.0"
url = "https://github.com/Bachmann1234/diff_cover"
source = f"$(PYPI_SITE)/d/diff_cover/diff_cover-{pkgver}.tar.gz"
sha256 = "391a37361aa9b4272c9b4301032b74e9cadc2acc1d6291d266b69e6f678996b1"
