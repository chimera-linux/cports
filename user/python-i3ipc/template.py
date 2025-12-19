pkgname = "python-i3ipc"
pkgver = "2.2.1"
pkgrel = 2
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-xlib"]
checkdepends = [
    "python-pytest",
    "python-pytest-asyncio",
    *depends,
]
pkgdesc = "Python library to control i3wm and sway"
license = "BSD-3-Clause"
url = "https://pypi.org/project/i3ipc"
source = f"$(PYPI_SITE)/i/i3ipc/i3ipc-{pkgver}.tar.gz"
sha256 = "e880d7d7147959ead5cb34764f08b97b41385b36eb8256e8af1ce163dbcccce8"
# test suite requires i3
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
