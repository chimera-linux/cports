pkgname = "libhangul"
pkgver = "0.2.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "gettext-devel", "libtool", "pkgconf"]
pkgdesc = "Library to support hangul input and character classification"
license = "LGPL-2.1-or-later"
url = "https://github.com/libhangul/libhangul"
source = f"{url}/archive/libhangul-{pkgver}.tar.gz"
sha256 = "db9a256ff1e2c639ea8168f5e8741dae95ad7ea563f257b1dbd098afd8e48487"
hardening = ["!vis", "!cfi"]


def post_extract(self):
    (self.cwd / "ChangeLog").touch()


@subpackage("libhangul-devel")
def _(self):
    return self.default_devel()


@subpackage("libhangul-progs")
def _(self):
    return self.default_progs()
