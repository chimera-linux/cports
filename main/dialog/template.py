pkgname = "dialog"
_mver = "1.3"
_date = "20211107"
pkgver = f"{_mver}.{_date}"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{_mver}-{_date}.tgz"
sha256 = "af97fd6787af2bd6df15de4d1fa4b5d57e22bc7b4c82d35661c21adb9520fdec"
options = ["lto"]

def post_install(self):
    self.rm(self.destdir / "usr/lib", force = True, recursive = True)
