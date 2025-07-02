pkgname = "python-diff-cover"
pkgver = "9.4.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-poetry-core",
]
depends = [
    "python-chardet",
    "python-jinja2",
    "python-pluggy",
    "python-pygments",
]
checkdepends = [
    "python-flake8",
    "python-pylint",
    "python-pytest",
    "python-pytest-datadir-nng",
    "python-pytest-mock",
    *depends,
]
pkgdesc = "Automatically find diff lines that need test coverage"
license = "Apache-2.0"
url = "https://github.com/Bachmann1234/diff_cover"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "31d609043721dc44491ae828ca478cc83099a1af931bb1607dc7752e69d69361"


def pre_check(self):
    self.mkdir("tests/data")
    self.mv(
        "tests/test_clover_violations_reporter/test.xml",
        "tests/data/test.xml",
    )
