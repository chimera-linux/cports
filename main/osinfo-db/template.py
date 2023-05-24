pkgname = "osinfo-db"
pkgver = "20230308"
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
sha256 = "546ba04ecc5e933ba2d7f3f3b4333a2980d4ae4dfc5284989b9c54758f2b9088"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz",
    )
