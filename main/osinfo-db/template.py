pkgname = "osinfo-db"
pkgver = "20230518"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = (
    f"https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz",
    False,
)
sha256 = "caec5bcce4f2f07c7006bb4f72913d12bdab52595011b4b50937fcd74b81cc6d"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz",
    )
