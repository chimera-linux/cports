pkgname = "gnome-user-docs"
pkgver = "50.0"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
hostmakedepends = [
    "gettext",
    "itstool",
    "libxml2-progs",
    "pkgconf",
]
makedepends = ["yelp"]
depends = ["yelp"]
pkgdesc = "User documentation for GNOME"
license = "CC-BY-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-user-docs"
source = f"$(GNOME_SITE)/gnome-user-docs/{pkgver[:-2]}/gnome-user-docs-{pkgver}.tar.xz"
sha256 = "e8e23324184c7e985c504f05f6d9c63420c9a9d1f64efde5da2a811236072f78"
options = ["!splitdoc"]
