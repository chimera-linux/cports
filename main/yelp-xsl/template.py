pkgname = "yelp-xsl"
pkgver = "42.4"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bash",
    "gettext",
    "itstool",
    "libxml2-progs",
    "libxslt-progs",
    "meson",
    "pkgconf",
]
makedepends = ["libxslt-devel"]
pkgdesc = "Help browser for GNOME desktop"
subdesc = "XSL and misc files"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Yelp/Xsl"
source = f"$(GNOME_SITE)/yelp-xsl/{pkgver[:-2]}/yelp-xsl-{pkgver}.tar.xz"
sha256 = "fdebb07eb2e66a7fb7a0dce6ad8248ad29a4bbb134ba829128ca104f58abd7d1"
