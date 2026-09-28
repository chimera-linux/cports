pkgname = "libdatrie"
pkgver = "0.2.13"
pkgrel = 0
build_style = "gnu_configure"
make_install_args = ["-j1"]
hostmakedepends = ["autoconf-archive", "automake", "pkgconf", "slibtool"]
pkgdesc = "Implementation of double-array structure for representing trie"
license = "LGPL-2.1-or-later"
url = "https://linux.thai.net/projects/datrie"
source = f"https://linux.thai.net/pub/ThaiLinux/software/libthai/libdatrie-{pkgver}.tar.xz"
sha256 = "12231bb2be2581a7f0fb9904092d24b0ed2a271a16835071ed97bed65267f4be"
# FIXME int
hardening = ["!int"]


@subpackage("libdatrie-devel")
def _(self):
    return self.default_devel()
