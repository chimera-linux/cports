pkgname = "yelp-xsl"
pkgver = "49.0"
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
sha256 = "59d43a8f8fe67b784f14f9a04dd4a7a092a7f4a64a65e71b90fe02a47a50fbec"
