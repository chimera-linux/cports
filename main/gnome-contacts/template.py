pkgname = "gnome-contacts"
pkgver = "50.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--libexecdir=/usr/libexec",  # TODO switch libexec
]
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
    "glycin-gtk4-devel",
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
sha256 = "2a3bea343171be244f12b7c21a40ca38e9a92dea9890393af5e8ac139bc0dab3"
options = ["!cross"]
