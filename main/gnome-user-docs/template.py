pkgname = "gnome-user-docs"
pkgver = "49.0"
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
sha256 = "ec118d44da1866e41738da19cf5dbc3d9a42925a2f3bf48ee6c37e6e3e46ddf3"
options = ["!splitdoc"]
