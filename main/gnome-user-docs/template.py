pkgname = "gnome-user-docs"
pkgver = "43.0"
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
sha256 = "3607160effd6f91e25a8798b57defb2099dd70b8fee4e7e2f20f2637ac28caee"
options = ["!splitdoc"]
