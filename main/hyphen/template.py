pkgname = "hyphen"
pkgver = "2.8.9"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."  # fails tests otherwise
hostmakedepends = ["automake", "pkgconf", "perl", "gawk", "libtool"]
checkdepends = ["bash"]
pkgdesc = "Hyphenation library"
license = "GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1"
url = "https://hunspell.github.io"
source = f"https://github.com/hunspell/hyphen/releases/download/v{pkgver}/hyphen-{pkgver}.tar.gz"
sha256 = "783743daf477de8c4d16e3c74b4d2827377017718d8e17e2d9440210246f6abe"


def post_install(self):
    self.install_license("COPYING")
    self.install_license("COPYING.MPL")


@subpackage("hyphen-devel")
def _(self):
    return self.default_devel()


@subpackage("hyphen-progs")
def _(self):
    return self.default_progs()
