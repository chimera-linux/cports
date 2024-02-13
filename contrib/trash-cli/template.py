pkgname = "trash-cli"
pkgver = "0.23.11.10"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-psutil", "python-six"]
pkgdesc = "Command line interface to the freedesktop.org trashcan"
maintainer = "Hugo Machet <mail@hmachet.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/andreafrancia/trash-cli"
source = f"https://github.com/andreafrancia/trash-cli/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "166a5b725c323a801b884b7040877788eefa592866149cf5647ef1fd3a14ceb9"
# unpackaged checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")
    self.install_man("man/man1/trash*.1", glob=True)
