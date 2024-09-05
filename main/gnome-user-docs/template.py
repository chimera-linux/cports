pkgname = "gnome-user-docs"
pkgver = "47_beta"
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
source = f"$(GNOME_SITE)/gnome-user-docs/{pkgver[:2]}/gnome-user-docs-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "57754f150915d909d019d2bd5af5eadb2532d1d12d05391d71a6c24835dac5a5"
options = ["!splitdoc"]
