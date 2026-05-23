pkgname = "dex"
pkgver = "0.10.1"
pkgrel = 0
build_style = "makefile"

_make_args = [f"VERSION=v{pkgver}"]

make_build_args = _make_args
make_install_args = [
    *_make_args,
    "PREFIX=/usr",
    "MANPREFIX=/usr/share/man",
]

hostmakedepends = ["python-sphinx"]
depends = ["python"]

pkgdesc = "DesktopEntry Execution"
license = "GPL-3.0-or-later"
url = "https://github.com/jceb/dex"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "661b96763b1cac062f872c78c03f150ed57d14e315720681bb1fb1e5362e29d4"


def check(self):
    self.do("./dex", "--test")
