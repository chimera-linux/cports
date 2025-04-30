pkgname = "python-jinja2"
pkgver = "3.1.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-flit_core",
    "python-installer",
]
checkdepends = ["python-pytest", "python-markupsafe"]
depends = ["python", "python-markupsafe"]
pkgdesc = "Python template engine"
license = "BSD-3-Clause"
url = "https://jinja.palletsprojects.com"
source = f"$(PYPI_SITE)/J/Jinja2/jinja2-{pkgver}.tar.gz"
sha256 = "0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d"
# dependency of pytest
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")
