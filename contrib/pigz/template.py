pkgname = "pigz"
pkgver = "2.8"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
makedepends = ["zlib-devel"]
pkgdesc = "Parallel implementation of gzip"
maintainer = "psykose <alice@ayaya.dev>"
license = "Zlib"
url = "https://github.com/madler/pigz"
source = f"https://zlib.net/pigz/pigz-{pkgver}.tar.gz"
sha256 = "eb872b4f0e1f0ebe59c9f7bd8c506c4204893ba6a8492de31df416f0d5170fd0"
hardening = ["vis", "cfi"]


def do_install(self):
    self.install_bin("pigz")
    self.install_bin("unpigz")
    self.install_man("pigz.1")
    self.install_link("pigz.1", "usr/share/man/man1/unpigz.1")
