pkgname = "gnome-user-docs"
pkgver = "47.0"
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
sha256 = "d06d87fcd726a90ed03a170cab45d470894991e312912fc508bde0dfbc83cfda"
options = ["!splitdoc"]
