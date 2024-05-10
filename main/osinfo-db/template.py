pkgname = "osinfo-db"
pkgver = "20240510"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz"
sha256 = "08a2d521c485687f6be39940d5b3f61bc0f583bb7e3655a131c658385eb7e5ca"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
