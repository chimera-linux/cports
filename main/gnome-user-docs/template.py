pkgname = "gnome-user-docs"
pkgver = "44.1"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "gettext-tiny",
    "itstool",
    "libxml2-progs",
]
makedepends = ["yelp"]
depends = ["yelp"]
pkgdesc = "User documentation for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-user-docs"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "93f3294d43fd22f9962ccf6bd17ff64eae78a6ca063fe6c1e9bc58d00f34e3a8"
options = ["!splitdoc"]
