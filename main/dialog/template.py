pkgname = "dialog"
pkgver = "1.3.20230209"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2023', '-2023')}.tgz"
sha256 = "0c26282305264be2217f335f3798f48b1dce3cf12c5a076bf231cadf77a6d6a8"
hardening = ["vis", "cfi"]

def post_install(self):
    self.rm(self.destdir / "usr/lib", force = True, recursive = True)

configure_gen = []
