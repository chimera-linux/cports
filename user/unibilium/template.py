pkgname = "unibilium"
pkgver = "2.1.4"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "libtool", "perl", "pkgconf"]
pkgdesc = "Simple, self-contained terminfo library"
license = "LGPL-3.0-or-later"
url = "https://github.com/neovim/unibilium"
source = f"https://github.com/neovim/unibilium/archive/v{pkgver}.tar.gz"
sha256 = "7360907bcf79ba49f6fc4a504767ff86e93ab9018477026fcc70d5ab77e1f2c1"
# crossbuild fails because of libtool
options = ["!cross"]


@subpackage("unibilium-devel")
def _(self):
    return self.default_devel()
