pkgname = "dialog"
pkgver = "1.3.20220728"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2022', '-2022')}.tgz"
sha256 = "54418973d559a461b00695fafe68df62f2bc73d506b436821d77ca3df454190b"
hardening = ["vis", "cfi"]

def post_install(self):
    self.rm(self.destdir / "usr/lib", force = True, recursive = True)
