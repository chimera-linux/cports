pkgname = "udisks"
pkgver = "2.9.4"
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
make_cmd = "gmake"
hostmakedepends = [
    "pkgconf",
    "gmake",
    "bash",
    "gobject-introspection",
    "docbook-xsl-nons",
    "gettext-tiny-devel",
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
source = f"https://github.com/storaged-project/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.bz2"
sha256 = "b6b60ebab0d5e09624120c5d158882e87d8c2473db60783b63deeba74cb18d1c"


def post_install(self):
    self.install_dir("var/lib/udisks2", mode=0o750, empty=True)


@subpackage("udisks-devel")
def _devel(self):
    return self.default_devel()


@subpackage("udisks-libs")
def _libs(self):
    return self.default_libs()
