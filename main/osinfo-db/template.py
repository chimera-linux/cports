pkgname = "osinfo-db"
pkgver = "20250124"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/osinfo-db-{pkgver}.tar.xz"
sha256 = "7ca717f0975a798135a2b39eefdd1436a0b0682e29685c7fd01ef7f83a257250"
options = ["!cross"]


def install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
