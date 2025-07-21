pkgname = "gnome-user-docs"
pkgver = "48.2"
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
sha256 = "67829f764ba672d7f99ff72ef6513b40cc931fb401bf7bd7db5f805e7bfa3db9"
options = ["!splitdoc"]
