pkgname = "yelp"
pkgver = "49.2"
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
sha256 = "5afc8e77308451ee45ee919efee5a154ca3c153a90e2a1b58cebf7827ab88ad0"


@subpackage("yelp-devel")
def _(self):
    return self.default_devel()
