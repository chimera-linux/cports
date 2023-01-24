pkgname = "gnome-disk-utility"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dlogind=libelogind"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "xsltproc",
    "docbook-xsl-nons", "desktop-file-utils",
]
makedepends = [
    "libdvdread-devel", "libglib-devel", "gtk+3-devel", "libhandy-devel",
    "liblzma-devel", "libnotify-devel", "libsecret-devel", "udisks-devel",
    "libpwquality-devel", "elogind-devel", "libcanberra-devel",
]
depends = ["udisks", "hicolor-icon-theme"]
pkgdesc = "GNOME disk drive and media management"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Disks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "7afca9805a6b92db6933dd7efcec4af8386c01bbc1f871e2dae4def7e192a2c5"
# FIXME cfi
hardening = ["vis", "!cfi"]
