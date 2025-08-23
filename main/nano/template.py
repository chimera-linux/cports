pkgname = "nano"
pkgver = "8.6"
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
sha256 = "f7abfbf0eed5f573ab51bd77a458f32d82f9859c55e9689f819d96fe1437a619"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_file("syntax/nanorc.nanorc", "usr/share/examples/nano")
