pkgname = "dex"
pkgver = "0.10.1"
pkgrel = 0
build_style = "makefile"
make_build_args = [f"VERSION=v{pkgver}"]
make_install_args = [
    "MANPREFIX=/usr/share/man",
    *make_build_args,
]
hostmakedepends = ["python-sphinx"]
depends = ["python"]
pkgdesc = "Program to generate/execute .desktop files"
license = "GPL-3.0-or-later"
url = "https://github.com/jceb/dex"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "661b96763b1cac062f872c78c03f150ed57d14e315720681bb1fb1e5362e29d4"


def check(self):
    self.do("./dex", "--test")
