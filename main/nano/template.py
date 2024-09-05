pkgname = "nano"
pkgver = "8.2"
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
sha256 = "d5ad07dd862facae03051c54c6535e54c7ed7407318783fcad1ad2d7076fffeb"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
