pkgname = "yelp"
pkgver = "42.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "bash",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "libxml2-devel",
    "libxslt-devel",
    "sqlite-devel",
    "webkitgtk-devel",
    "yelp-xsl",
]
depends = ["dconf", "yelp-xsl"]
pkgdesc = "Help browser for GNOME desktop"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Yelp"
source = f"$(GNOME_SITE)/yelp/{pkgver[:-2]}/yelp-{pkgver}.tar.xz"
sha256 = "26ccc422679a9e6a7a3aa083d90fcdb347f5f2300be3e01431a30d0cdd2a89a3"


@subpackage("yelp-devel")
def _(self):
    return self.default_devel()
