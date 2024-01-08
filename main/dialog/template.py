pkgname = "dialog"
pkgver = "1.3.20240101"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-ncursesw", "--disable-nls"]
# broken to reconf
configure_gen = []
makedepends = ["ncurses-devel"]
pkgdesc = "Tool to display dialog boxes from shell scripts"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-only"
url = "https://invisible-island.net/dialog"
source = f"https://invisible-mirror.net/archives/{pkgname}/{pkgname}-{pkgver.replace('.2024', '-2024')}.tgz"
sha256 = "9419eb52b95837312a76ccb26002c5d624fab53abde0859f1c7364179dc0ebad"
hardening = ["vis", "cfi"]


def post_install(self):
    self.rm(self.destdir / "usr/lib", force=True, recursive=True)
