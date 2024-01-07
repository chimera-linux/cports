pkgname = "clickclack"
pkgver = "0.2.3"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers", "sdl-devel"]
pkgdesc = "Haptic and audio feedback utility"
maintainer = "Froggo <froggo8311@proton.me>"
license = "MIT"
url = "https://git.sr.ht/~proycon/clickclack"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "940f13ae1aa8b33677d8153db4af848233cb45dbb755320463dc3f980c73cced"
# no tests
options = ["!check"]


def do_install(self):
    self.install_bin("clickclack")
    self.install_license("LICENSE")
