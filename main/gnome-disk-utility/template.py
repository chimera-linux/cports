pkgname = "gnome-disk-utility"
pkgver = "45.0"
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
depends = ["udisks", "desktop-file-utils"]
pkgdesc = "GNOME disk drive and media management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "3d8625faa99047bc4aefd29921ad728ab4d700cff86e0f2ec67e8dba877d0dd3"
# FIXME cfi
hardening = ["vis", "!cfi"]
