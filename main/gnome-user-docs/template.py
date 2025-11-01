pkgname = "gnome-user-docs"
pkgver = "49.1"
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
sha256 = "0e50b8bb4fceaa9128367cd3458e5edb861c96278c1aa9a73a6ec0402b7bc617"
options = ["!splitdoc"]
