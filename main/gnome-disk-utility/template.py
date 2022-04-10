pkgname = "gnome-disk-utility"
pkgver = "42.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlogind=libelogind"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "xsltproc",
    "docbook-xsl-nons",
]
makedepends = [
    "libdvdread-devel", "libglib-devel", "gtk+3-devel", "libhandy-devel",
    "liblzma-devel", "libnotify-devel", "libsecret-devel", "udisks-devel",
    "libpwquality-devel", "elogind-devel", "libcanberra-devel",
]
depends = ["hicolor-icon-theme"]
pkgdesc = "GNOME disk drive and media management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1b6564454d67426322cb3bfc5a5558653bfc7dfeea2ae0825b1d08629f01090b"
