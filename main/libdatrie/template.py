pkgname = "libdatrie"
pkgver = "0.2.13"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
make_install_args = ["-j1"]
hostmakedepends = ["gmake", "pkgconf"]
pkgdesc = "Implementation of double-array structure for representing trie"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://linux.thai.net/projects/datrie"
source = f"https://linux.thai.net/pub/ThaiLinux/software/libthai/{pkgname}-{pkgver}.tar.xz"
sha256 = "12231bb2be2581a7f0fb9904092d24b0ed2a271a16835071ed97bed65267f4be"
# FIXME int
hardening = ["!int"]

@subpackage("libdatrie-devel")
def _devel(self):
    return self.default_devel()

configure_gen = []
