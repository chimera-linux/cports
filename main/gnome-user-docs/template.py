pkgname = "gnome-user-docs"
pkgver = "46.4"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = [
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
source = f"$(GNOME_SITE)/gnome-user-docs/{pkgver[:-2]}/gnome-user-docs-{pkgver}.tar.xz"
sha256 = "2776072f15f92bd05028345f3ac8a093d44260de52a620d62693c0e5eea20534"
options = ["!splitdoc"]
