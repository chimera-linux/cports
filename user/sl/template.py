pkgname = "sl"
pkgver = "5.05"
pkgrel = 0
build_style = "makefile"
makedepends = ["ncurses-devel"]
pkgdesc = "Steam Locomotive"
license = "SL"
url = "https://github.com/eyJhb/sl"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "6c941b526e3d01be7f91a3af4ae20a89d1e5d66b3b2d804c80123b1b1be96384"
hardening = ["vis", "cfi"]
# No test suite
options = ["!check"]


def install(self):
    self.install_bin("sl")
    self.install_man("sl.1")
    self.install_man("sl.1.ja", "sl", 1, lang="ja")
    self.install_license("LICENSE")
