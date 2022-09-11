pkgname = "osinfo-db"
pkgver = "20220830"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = (f"https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz", False)
sha256 = "8111643d90deab838db7f213f154bef2e057350a9c834245ee01dd64433baafb"
options = ["!cross"]

def do_install(self):
    self.do("osinfo-db-import", "--root", self.chroot_destdir, "--system", f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz")
