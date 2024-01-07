pkgname = "libhangul"
pkgver = "0.1.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["./autogen.sh"]
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
pkgdesc = "Library to support hangul input and character classification"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/libhangul/libhangul"
source = f"{url}/archive/{pkgname}-{pkgver}.tar.gz"
sha256 = "e2a81ef159ed098d3cc1a20377dba6204821b7ce2bc24cfb2f2543adf3bc5830"
# FIXME enable vis and cfi, build currently fails with vis


@subpackage("libhangul-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libhangul-progs")
def _progs(self):
    return self.default_progs()
