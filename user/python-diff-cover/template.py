pkgname = "python-diff-cover"
pkgver = "9.2.4"
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
sha256 = "6ea44711f09199a1b8bcaa2eae002e1f337dd22f2d798fcfd62a6a1554bb2a86"
