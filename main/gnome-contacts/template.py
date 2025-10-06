pkgname = "gnome-contacts"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "blueprint-compiler",
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
sha256 = "25f21c67bc29d77def2d9cd3e22d28460d12b47ff248a2017731b54db485e4af"
options = ["!cross"]
