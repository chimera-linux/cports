pkgname = "telepathy-mission-control"
pkgver = "5.16.6"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gtk-doc-tools",
    "libtool",
    "pkgconf",
    "xsltproc",
]
makedepends = ["dbus-devel", "dbus-glib-devel", "telepathy-glib-devel"]
pkgdesc = "Account manager and channel dispatcher for the Telepathy framework"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "LGPL-2.1-only"
url = "https://telepathy.freedesktop.org"
source = f"{url}/releases/telepathy-mission-control/telepathy-mission-control-{pkgver}.tar.gz"
sha256 = "2df8ae3995e919a7670e01aa3568215ef0777e34961ace1cac1c6477cb297a45"


@subpackage("telepathy-mission-control-devel")
def _(self):
    return self.default_devel()
