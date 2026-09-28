pkgname = "osinfo-db"
pkgver = "20250606"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://releases.pagure.org/libosinfo/osinfo-db-{pkgver}.tar.xz"
sha256 = "9940aa47df298073c51dcf8a4dcc855f494ab864c24cdbda46bd897957357fe1"
options = ["!cross"]


def install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
