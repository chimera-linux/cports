pkgname = "unibilium"
pkgver = "2.1.2"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["automake", "libtool", "perl", "pkgconf"]
pkgdesc = "Simple, self-contained terminfo library"
maintainer = "yopito <pierre.bourgin@free.fr>"
license = "LGPL-3.0-or-later"
url = "https://github.com/neovim/unibilium"
source = f"https://github.com/neovim/unibilium/archive/v{pkgver}.tar.gz"
sha256 = "370ecb07fbbc20d91d1b350c55f1c806b06bf86797e164081ccc977fc9b3af7a"
# crossbuild fails because of libtool
options = ["!cross"]


@subpackage("unibilium-devel")
def _(self):
    return self.default_devel()
