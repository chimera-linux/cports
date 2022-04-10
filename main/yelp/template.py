pkgname = "yelp"
pkgver = "42.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-schemas-compile", "--disable-static",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "glib-devel", "pkgconf", "gettext-tiny", "itstool",
]
makedepends = [
    "libglib-devel", "gtk+3-devel", "libhandy-devel", "libxml2-devel",
    "libxslt-devel", "sqlite-devel", "webkitgtk-devel", "yelp-xsl"
]
depends = ["dconf", "yelp-xsl", "hicolor-icon-theme"]
pkgdesc = "Help browser for GNOME desktop"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Yelp"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "25b1146ab8549888a5a8da067f63b470b0f0f800b6ae889cacd114d01d713b41"

@subpackage("yelp-devel")
def _devel(self):
    return self.default_devel()
