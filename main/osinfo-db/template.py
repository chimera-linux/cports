pkgname = "osinfo-db"
pkgver = "20260812"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = f"!https://gitlab.com/libosinfo/osinfo-db/-/releases/v{pkgver}/downloads/osinfo-db-{pkgver}.tar.xz"
sha256 = "f13ed6e1e480b5266d39cad7f0010febdf0265dfc45579de2fb34543bc6b35de"
options = ["!cross"]


def install(self):
    self.do(
        "osinfo-db-import",
        "--root",
        self.chroot_destdir,
        "--system",
        self.chroot_sources_path / f"{pkgname}-{pkgver}.tar.xz",
    )
