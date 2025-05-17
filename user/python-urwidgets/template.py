pkgname = "python-urwidgets"
pkgver = "0.2.1"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-wheel",
    "python-setuptools",
]
depends = ["python-urwid"]
pkgdesc = "Collection of widgets for urwid"
license = "MIT"
url = "https://github.com/AnonymouX47/urwidgets"
source = f"$(PYPI_SITE)/u/urwidgets/urwidgets-{pkgver}.tar.gz"
sha256 = "f9f2bcd2949da1105c287806dab773aa7bdf5852226cdb128aaf3004136f3eef"
# no tests defined
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
