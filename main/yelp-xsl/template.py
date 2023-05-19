pkgname = "yelp-xsl"
pkgver = "42.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf", "gettext-tiny", "itstool"]
makedepends = ["libxslt-devel"]
pkgdesc = "Help browser for GNOME desktop (XSL and misc files)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Yelp/Xsl"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "238be150b1653080ce139971330fd36d3a26595e0d6a040a2c030bf3d2005bcd"

configure_gen = []
