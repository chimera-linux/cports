pkgname = "gnome-user-docs"
pkgver = "48.1"
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
sha256 = "ac973d924e00545a1458d86a110d4773e6bbe37c372840d76ed640cb268c61fd"
options = ["!splitdoc"]
