pkgname = "osinfo-db"
pkgver = "20231215"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz"
sha256 = "dfb7c5975ce4efffd92aadd00094a0f7c593b41988fda539915f6459f7164554"
options = ["!cross"]


def do_install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
