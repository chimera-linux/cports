pkgname = "osinfo-db"
pkgver = "20230719"
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
sha256 = "13d1c97fc7d67137935dcc97778c08bb079a4f0fe312d479786cea1411e4845a"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz",
    )
