pkgname = "dialog"
pkgver = "1.3.20220117"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2022', '-2022')}.tgz"
sha256 = "754cb6bf7dc6a9ac5c1f80c13caa4d976e30a5a6e8b46f17b3bb9b080c31041f"

def post_install(self):
    self.rm(self.destdir / "usr/lib", force = True, recursive = True)
