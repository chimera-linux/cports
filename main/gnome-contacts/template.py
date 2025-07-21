pkgname = "gnome-contacts"
pkgver = "48.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "gtk+3-update-icon-cache",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "vala",
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
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Contacts"
source = f"$(GNOME_SITE)/gnome-contacts/{pkgver.split('.')[0]}/gnome-contacts-{pkgver}.tar.xz"
sha256 = "a2762995b59427ec3f185f28b5594e37077b72a70cd7c19217ed634637ecc1b5"
options = ["!cross"]
