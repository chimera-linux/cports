pkgname = "gnome-user-docs"
pkgver = "44.0"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "gettext-tiny", "itstool", "libxml2-progs"
]
makedepends = ["yelp"]
depends = ["yelp"]
pkgdesc = "User documentation for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CC-BY-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-user-docs"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "cf6cd7eb9c4149dd93966f71fa1b907afc8f651ecc3af54e1085bcf4ad21b1bd"
options = ["!splitdoc"]

configure_gen = []
