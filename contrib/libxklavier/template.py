pkgname = "libxklavier"
pkgver = "5.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-xkb-bin-base=/usr/bin",
]
make_cmd = "gmake"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    # TODO: cause a bunch of build warnings, e.g.:
    # ../../libxklavier/xkl_config_registry.h:132: Warning: Xkl: symbol='ConfigItemProcessFunc': Unknown namespace for identifier 'ConfigItemProcessFunc'
    # "gobject-introspection",
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
pkgdesc = "High-level API for X Keyboard Extension (deprecated)"
maintainer = "triallax <triallax@tutanota.com>"
license = "LGPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/LibXklavier"
source = f"https://people.freedesktop.org/~svu/libxklavier-{pkgver}.tar.bz2"
sha256 = "17a34194df5cbcd3b7bfd0f561d95d1f723aa1c87fca56bc2c209514460a9320"


@subpackage("libxklavier-devel")
def _devel(self):
    return self.default_devel()
