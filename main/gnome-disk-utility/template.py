pkgname = "gnome-disk-utility"
pkgver = "41.0"
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
sha256 = "8743c98fd656062ef862933efe30c5be4c6b322ec02eee154ec70d08ed0895df"
