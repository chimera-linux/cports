pkgname = "gnome-user-docs"
pkgver = "42.0"
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
sha256 = "b2b27da04100bbdd2f4f0e5bc38f2d056d95fa3656720163f6436a3167d5e905"
options = ["!splitdoc"]
