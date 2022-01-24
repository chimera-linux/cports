pkgname = "yelp"
pkgver = "41.2"
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
sha256 = "b00bf033f02dd79b6d3f255031c71df8d6ed38e552c870b8f391a374724c43c5"

@subpackage("yelp-devel")
def _devel(self):
    return self.default_devel()
