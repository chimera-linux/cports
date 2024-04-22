pkgname = "gnome-user-docs"
pkgver = "46.1"
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
sha256 = "a97293cbeeb797eb4f4d169d713bb6583bd12c3791e140283e4356d2fe180ada"
options = ["!splitdoc"]
