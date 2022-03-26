pkgname = "osinfo-db"
pkgver = "20220214"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = (f"https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz", False)
sha256 = "13e6c900eb8200f1660f8a1ed775ececd5a01fdb24bfb6eee1ce65dd7bcfd3a9"
options = ["!cross"]

def do_install(self):
    self.do("osinfo-db-import", "--root", self.chroot_destdir, "--system", f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz")
