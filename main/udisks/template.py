pkgname = "udisks"
pkgver = "2.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-udevdir=/usr/lib/udev",
    "--enable-lvm2",
    "--enable-btrfs",
    "--enable-bcache",
    "--enable-vdo",
    "--enable-lvmcache",
    "--enable-introspection",
]
hostmakedepends = [
    "pkgconf",
    "bash",
    "gobject-introspection",
    "docbook-xsl-nons",
    "gettext-devel",
    "glib-devel",
    "xsltproc",
    "polkit",
    "automake",
    "libtool",
    "gtk-doc-tools",
]
makedepends = [
    "acl-devel",
    "libatasmart-devel",
    "libgudev-devel",
    "polkit-devel",
    "elogind-devel",
    "libblockdev-devel",
    "libbtrfs-devel",
    "device-mapper-devel",
]
pkgdesc = "Daemon, tools and libraries for disk manipulation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/udisks"
source = f"https://github.com/storaged-project/udisks/releases/download/udisks-{pkgver}/udisks-{pkgver}.tar.bz2"
sha256 = "b75734ccf602540dedb4068bec206adcb508a4c003725e117ae8f994d92d8ece"


def post_install(self):
    self.install_dir("var/lib/udisks2", mode=0o750, empty=True)


@subpackage("udisks-devel")
def _(self):
    return self.default_devel()


@subpackage("udisks-libs")
def _(self):
    return self.default_libs()
