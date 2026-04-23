pkgname = "nano"
pkgver = "9.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-utf8"]
# fails to regen
configure_gen = []
makedepends = ["ncurses-devel", "file-devel", "linux-headers"]
pkgdesc = "GNU nano text editor"
license = "GPL-3.0-or-later"
url = "https://www.nano-editor.org"
source = f"{url}/dist/v{pkgver[0]}/nano-{pkgver}.tar.xz"
sha256 = "9f384374b496110a25b73ad5a5febb384783c6e3188b37063f677ac908013fde"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
