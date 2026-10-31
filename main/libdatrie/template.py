pkgname = "libdatrie"
pkgver = "0.2.14"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["autoconf-archive", "automake", "libtool", "pkgconf"]
pkgdesc = "Implementation of double-array structure for representing trie"
license = "LGPL-2.1-or-later"
url = "https://linux.thai.net/projects/datrie"
source = f"https://linux.thai.net/pub/ThaiLinux/software/libthai/libdatrie-{pkgver}.tar.xz"
sha256 = "f04095010518635b51c2313efa4f290b7db828d6273e39b2b8858f859dfe81d5"
# FIXME int
hardening = ["!int"]


@subpackage("libdatrie-devel")
def _(self):
    return self.default_devel()
