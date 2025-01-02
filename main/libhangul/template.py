pkgname = "libhangul"
pkgver = "0.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
pkgdesc = "Library to support hangul input and character classification"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libhangul/libhangul"
source = f"{url}/archive/libhangul-{pkgver}.tar.gz"
sha256 = "e2a81ef159ed098d3cc1a20377dba6204821b7ce2bc24cfb2f2543adf3bc5830"
hardening = ["!vis", "!cfi"]


def post_extract(self):
    (self.cwd / "ChangeLog").touch()


@subpackage("libhangul-devel")
def _(self):
    return self.default_devel()


@subpackage("libhangul-progs")
def _(self):
    return self.default_progs()
