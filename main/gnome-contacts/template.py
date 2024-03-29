pkgname = "gnome-contacts"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "docbook-xsl-nons",
    "gettext",
    "gobject-introspection",
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
source = (
    f"$(GNOME_SITE)/{pkgname}/{pkgver.split('.')[0]}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "70aeb4e835a1c77f9bcc7e57a2dcc2376d93bdb617571618257445f56c6370df"
options = ["!cross"]
