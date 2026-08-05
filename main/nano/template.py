pkgname = "nano"
pkgver = "9.2"
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
sha256 = "05ecb99247b782e8a5b3a25ed4101dd034b0236902f7449bc9795b717642f7e9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
