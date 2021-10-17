pkgname = "dialog"
_mver = "1.3"
_date = "20210621"
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
sha256 = "c3af22ccfcd9baca384062108dd9354e86990929ee270c239eef69518c5da7c8"

def post_install(self):
    self.rm(self.destdir / "usr/lib", force = True, recursive = True)
