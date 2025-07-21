pkgname = "python-idna"
pkgver = "3.10"
pkgrel = 1
build_style = "python_pep517"
make_check_target = "tests"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest"]
depends = ["python"]
pkgdesc = "Internationalized Domain Names in Applications (IDNA) for Python"
license = "BSD-3-Clause"
url = "https://github.com/kjd/idna"
source = f"$(PYPI_SITE)/i/idna/idna-{pkgver}.tar.gz"
sha256 = "12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9"
# dep cycle with pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
