pkgname = "osinfo-db"
pkgver = "20231027"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz"
sha256 = "84a3dd050786ad52215fa3ec6531573ee6b3c3a56ca20b1ba75b2d85e0f0ba1a"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz",
    )
