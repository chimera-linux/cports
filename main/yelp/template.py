pkgname = "yelp"
pkgver = "42.2"
pkgrel = 4
build_style = "gnu_configure"
configure_args = [
    "--disable-schemas-compile",
    "--disable-static",
]
configure_gen = []
hostmakedepends = [
    "glib-devel",
    "pkgconf",
    "gettext",
    "itstool",
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
sha256 = "a2c5fd0787a9089c722cc66bd0f85cdf7088d870e7b6cc85799f8e5bff9eac4b"


@subpackage("yelp-devel")
def _(self):
    return self.default_devel()
