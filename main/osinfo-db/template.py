pkgname = "osinfo-db"
pkgver = "20240701"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/osinfo-db-{pkgver}.tar.xz"
sha256 = "1d7381a72f0c45f473befa4a92fa010a37fc4f7b2bb5d1f68e06da440ef6905d"
options = ["!cross"]


def install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
