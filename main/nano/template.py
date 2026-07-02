pkgname = "nano"
pkgver = "9.1"
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
sha256 = "5f47764274cb7532349ce0aa20ec10f1e8e851a6e9fa3eb66812c43d196db042"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
