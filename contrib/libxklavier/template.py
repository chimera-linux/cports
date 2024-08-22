pkgname = "libxklavier"
pkgver = "5.4"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-xkb-bin-base=/usr/bin",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gobject-introspection",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "iso-codes",
    "libx11-devel",
    "libxi-devel",
    "libxkbfile-devel",
    "libxml2-devel",
]
depends = ["iso-codes", "xkeyboard-config"]
pkgdesc = "Deprecated high-level API for X Keyboard Extension"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/LibXklavier"
source = f"https://people.freedesktop.org/~svu/libxklavier-{pkgver}.tar.bz2"
sha256 = "17a34194df5cbcd3b7bfd0f561d95d1f723aa1c87fca56bc2c209514460a9320"
options = ["!cross"]


@subpackage("libxklavier-devel")
def _(self):
    return self.default_devel()
