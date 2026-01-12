pkgname = "nano"
pkgver = "8.7"
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
sha256 = "afd287aa672c48b8e1a93fdb6c6588453d527510d966822b687f2835f0d986e9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
