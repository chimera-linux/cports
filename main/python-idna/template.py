pkgname = "python-idna"
pkgver = "3.16"
pkgrel = 0
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
sha256 = "d7a6da03db833450fca25d2358ac9ff06cd624577a4aea3a596d5c0f77b8e03d"
# dep cycle with pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
