pkgname = "unibilium"
pkgver = "2.1.1"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
hostmakedepends = ["gmake", "libtool", "perl", "pkgconf"]
pkgdesc = "Simple, self-contained terminfo library"
license = "LGPL-3.0-or-later"
url = "https://github.com/neovim/unibilium"
source = f"https://github.com/neovim/unibilium/archive/v{pkgver}.tar.gz"
sha256 = "6f0ee21c8605340cfbb458cbd195b4d074e6d16dd0c0e12f2627ca773f3cabf1"
# crossbuild fails because of libtool
options = ["!cross"]


@subpackage("unibilium-devel")
def _devel(self):
    return self.default_devel()
