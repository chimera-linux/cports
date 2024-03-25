pkgname = "gnome-disk-utility"
pkgver = "46.0"
pkgrel = 0
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
sha256 = "464649148c6d6771f1ac2ebfe43a4e519205b11c2d914a09f2a001821d06957d"
