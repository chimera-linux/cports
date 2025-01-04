pkgname = "nano"
pkgver = "8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
# fails to regen
configure_gen = []
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"https://www.nano-editor.org/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "551b717b2e28f7e90f749323686a1b5bbbd84cfa1390604d854a3ca3778f111e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
