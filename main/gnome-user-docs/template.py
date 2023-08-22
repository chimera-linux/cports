pkgname = "gnome-user-docs"
pkgver = "44.3"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "gettext",
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
sha256 = "94e044082363438bcdbfa8549489ab6ab296a091e8b652f572133fd74db1692c"
options = ["!splitdoc"]
