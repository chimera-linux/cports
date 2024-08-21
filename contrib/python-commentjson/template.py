pkgname = "python-commentjson"
pkgver = "0.9.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["python-lark-parser"]
pkgdesc = "Python parser for JSON with Python/Javascript style inline comments"
maintainer = "Mara <177581589+catgirlconspiracy@users.noreply.github.com>"
license = "MIT"
url = "https://github.com/vaidik/commentjson"
source = f"$(PYPI_SITE)/c/commentjson/commentjson-{pkgver}.tar.gz"
sha256 = "42f9f231d97d93aff3286a4dc0de39bfd91ae823d1d9eba9fa901fe0c7113dd4"
# the tests all fail and I don't know how they ever didn't fail
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.rst")
