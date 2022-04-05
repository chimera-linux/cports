pkgname = "nano"
pkgver = "6.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"https://www.nano-editor.org/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "2bca1804bead6aaf4ad791f756e4749bb55ed860eec105a97fba864bc6a77cb3"

def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
