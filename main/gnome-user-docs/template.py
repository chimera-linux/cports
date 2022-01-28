pkgname = "gnome-user-docs"
pkgver = "41.1"
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
sha256 = "55ee3df577d1717fc152fc2aeb89d0af7a9eca866c8974c675f60bd630888c48"
options = ["!splitdoc"]
