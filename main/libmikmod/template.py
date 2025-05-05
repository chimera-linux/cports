pkgname = "libmikmod"
pkgver = "3.3.13"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake", "libtool", "pkgconf"]
pkgdesc = "Mikmod module player and library"
license = "LGPL-2.1-or-later"
url = "http://mikmod.shlomifish.org"
source = f"$(SOURCEFORGE_SITE)/mikmod/libmikmod-{pkgver}.tar.gz"
sha256 = "9fc1799f7ea6a95c7c5882de98be85fc7d20ba0a4a6fcacae11c8c6b382bb207"
# CFI: crashes in sc2 ucm
hardening = ["vis", "!cfi"]


@subpackage("libmikmod-devel")
def _(self):
    return self.default_devel(extra=["usr/share/info"])
