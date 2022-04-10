pkgname = "yelp-tools"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "itstool",
    "python-lxml", "xsltproc", "libxml2-progs"
]
makedepends = ["yelp-xsl"]
depends = ["xsltproc", "yelp-xsl", "python-lxml"]
pkgdesc = "Help browser for GNOME desktop (XSL and misc files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/yelp-tools"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "2cd43063ffa7262df15dd8d379aa3ea3999d42661f07563f4802daa1149f7df4"
