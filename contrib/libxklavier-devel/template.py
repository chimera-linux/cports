pkgname = "libxklavier"
pkgver = "5.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static", "--with-introspection",
]
hostmakedepends = ["pkgconf", "glib-devel"]
makedepends = [
    "glib-devel", "libxkbfile-devel", "libxml2-devel", "libxi-devel", "xkeyboard-config", "iso-codes"
]
pkgdesc = "Library providing high-level API for X Keyboard Extension"
maintainer = "toukoAMG <toukoamg@tutanota.com>"
license = "LGPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/LibXklavier"
source = f"https://people.freedesktop.org/~svu/{pkgname}-{pkgver}.tar.bz2"
sha256 = "17a34194df5cbcd3b7bfd0f561d95d1f723aa1c87fca56bc2c209514460a9320"

@subpackage("libxklavier-devel")
def _dev(self):
    return self.default_devel()
