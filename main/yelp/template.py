pkgname = "yelp"
pkgver = "49.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "bash",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libxml2-devel",
    "libxslt-devel",
    "sqlite-devel",
    "webkitgtk4-devel",
    "yelp-xsl",
]
depends = ["dconf", "yelp-xsl"]
pkgdesc = "Help browser for GNOME desktop"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Yelp"
source = f"$(GNOME_SITE)/yelp/{pkgver[:-2]}/yelp-{pkgver}.tar.xz"
sha256 = "3e3e94ef2d2c9487cc51062e3afbfa1578cebd29d80c84357b6d7ee6dcfd8a74"


@subpackage("yelp-devel")
def _(self):
    return self.default_devel()
