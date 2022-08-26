pkgname = "osinfo-db"
pkgver = "20220727"
pkgrel = 0
hostmakedepends = ["osinfo-db-tools"]
pkgdesc = "Osinfo database of information about operating systems"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://libosinfo.org"
source = (f"https://releases.pagure.org/libosinfo/{pkgname}-{pkgver}.tar.xz", False)
sha256 = "2291e5234ed899a830c36f2b4056ff5e76235f4ba07b593421f4865290634d5e"
options = ["!cross"]

def do_install(self):
    self.do("osinfo-db-import", "--root", self.chroot_destdir, "--system", f"/sources/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.xz")
