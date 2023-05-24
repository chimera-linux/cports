pkgname = "nano"
pkgver = "7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"https://www.nano-editor.org/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "86f3442768bd2873cec693f83cdf80b4b444ad3cc14760b74361474fc87a4526"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")


configure_gen = []
