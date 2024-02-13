pkgname = "gnome-disk-utility"
pkgver = "45.1"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dlogind=libelogind"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "xsltproc",
    "docbook-xsl-nons",
    "desktop-file-utils",
]
makedepends = [
    "libdvdread-devel",
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "xz-devel",
    "libnotify-devel",
    "libsecret-devel",
    "udisks-devel",
    "libpwquality-devel",
    "elogind-devel",
    "libcanberra-devel",
]
depends = ["udisks"]
pkgdesc = "GNOME disk drive and media management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "540ff4ec9a6b9630003ff4cd60d624f39fe70f25a9559e5333389603c85b9529"
