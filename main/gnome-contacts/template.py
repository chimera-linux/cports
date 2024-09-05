pkgname = "gnome-contacts"
pkgver = "47_alpha"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "gtk-update-icon-cache",
    "meson",
    "pkgconf",
    "vala",
    "xsltproc",
]
makedepends = [
    "evolution-data-server-devel",
    "folks-devel",
    "glib-devel",
    "gnome-online-accounts-devel",
    "gstreamer-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libportal-devel",
    "qrencode-devel",
]
pkgdesc = "GNOME contacts application"
maintainer = "triallax <triallax@tutanota.com>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Contacts"
source = f"$(GNOME_SITE)/gnome-contacts/{pkgver[:2]}/gnome-contacts-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "492c7f7616f26f1fa5210d52585ce9f714c1d9bde7d2c352fcf6f21c48d8637c"
options = ["!cross"]
