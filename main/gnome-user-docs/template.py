pkgname = "gnome-user-docs"
pkgver = "47.5"
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
license = "CC-BY-3.0"
url = "https://gitlab.gnome.org/GNOME/gnome-user-docs"
source = f"$(GNOME_SITE)/gnome-user-docs/{pkgver[:-2]}/gnome-user-docs-{pkgver}.tar.xz"
sha256 = "727cd30d80a801412be4085bfedc870f962a49fd057d904c6d42534bae1f2133"
options = ["!splitdoc"]
