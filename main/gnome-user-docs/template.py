pkgname = "gnome-user-docs"
pkgver = "51.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "gettext",
    "itstool",
    "libxml2-progs",
    "meson",
    "ninja",
    "pkgconf",
    "yelp-tools",
]
makedepends = ["yelp"]
depends = ["yelp"]
pkgdesc = "User documentation for GNOME"
license = "CC-BY-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-user-docs"
source = f"$(GNOME_SITE)/gnome-user-docs/{pkgver[:-2]}/gnome-user-docs-{pkgver}.tar.xz"
sha256 = "bf3ebd7fa1da70617884b07392de8d605305cfef71c2e883749cb08ff0d6a7d1"
# meh
options = ["!splitdoc", "!check"]
