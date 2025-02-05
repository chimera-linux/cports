pkgname = "yelp-tools"
pkgver = "42.1"
pkgrel = 2
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "gettext",
    "itstool",
    "python-lxml",
    "libxslt-progs",
    "libxml2-progs",
]
makedepends = ["yelp-xsl"]
depends = ["libxslt-progs", "yelp-xsl", "python-lxml"]
pkgdesc = "Help browser for GNOME desktopS"
subdesc = "tools"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/yelp-tools"
source = f"$(GNOME_SITE)/yelp-tools/{pkgver[:-2]}/yelp-tools-{pkgver}.tar.xz"
sha256 = "3e496a4020d4145b99fd508a25fa09336a503a4e8900028421e72c6a4b11f905"
hardening = ["vis", "cfi"]
