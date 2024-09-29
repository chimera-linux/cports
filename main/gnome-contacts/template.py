pkgname = "gnome-contacts"
pkgver = "47.0"
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
source = f"$(GNOME_SITE)/gnome-contacts/{pkgver.split('.')[0]}/gnome-contacts-{pkgver}.tar.xz"
sha256 = "25e3c6f79728188afa5f0cd5d0be85dc467d12db6a2d98b54af3df0dcb4290d0"
options = ["!cross"]
