pkgname = "osinfo-db"
pkgver = "20221018"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = (f"https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz", False)
sha256 = "96736156d40fc8bcaadd4e843fe4ac8189818c06794f3171e9ce2ec21abab886"
options = ["!cross"]

def do_install(self):
    self.do("osinfo-db-import", "--root", self.chroot_destdir, "--system", f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz")
