pkgname = "gnome-disk-utility"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlogind=libelogind"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "xsltproc",
    "docbook-xsl-nons", "desktop-file-utils",
]
makedepends = [
    "libdvdread-devel", "glib-devel", "gtk+3-devel", "libhandy-devel",
    "liblzma-devel", "libnotify-devel", "libsecret-devel", "udisks-devel",
    "libpwquality-devel", "elogind-devel", "libcanberra-devel",
]
depends = ["udisks", "hicolor-icon-theme"]
pkgdesc = "GNOME disk drive and media management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "02031097896cdb37d8717a5823f93e3723d4dfce7fdc4002c9dfcb16b7e7a3ef"
# FIXME cfi
hardening = ["vis", "!cfi"]
