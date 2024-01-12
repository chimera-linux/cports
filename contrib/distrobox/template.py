pkgname = "distrobox"
pkgver = "1.6.0.1"
pkgrel = 0
pkgdesc = "Use any Linux distribution inside your terminal"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://distrobox.it"
source = f"https://github.com/89luca89/distrobox/archive/{pkgver}.tar.gz"
sha256 = "d6b1330b56f6a1bf844c26a27d87f39efd8ae088ed3063f6513d48cf9c18f57e"


def do_install(self):
    self.do("./install", "--prefix", self.destdir / "usr", "-v")
    self.install_files("docs/*.md", f"usr/share/docs/{pkgname}")
