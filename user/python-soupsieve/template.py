pkgname = "python-soupsieve"
pkgver = "2.7"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-hatchling",
    "python-installer",
]
checkdepends = ["python-beautifulsoup4", "python-pytest"]
pkgdesc = "CSS selector implementation for python-beautifulsoup"
license = "MIT"
url = "https://github.com/facelessuser/soupsieve"
source = f"$(PYPI_SITE)/s/soupsieve/soupsieve-{pkgver}.tar.gz"
sha256 = "ad282f9b6926286d2ead4750552c8a6142bc4c783fd66b0293547c8fe6ae126a"
# cyclic dep bs4 -> soupsieve -> bs4
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.md")
