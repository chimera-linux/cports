pkgname = "nano"
pkgver = "6.4"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"https://www.nano-editor.org/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "4199ae8ca78a7796de56de1a41b821dc47912c0307e9816b56cc317df34661c0"

def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")

# FIXME visibility
hardening = ["!vis"]
