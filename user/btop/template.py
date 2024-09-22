pkgname = "btop"
pkgver = "1.4.0"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
pkgdesc = "TUI monitor of system resources"
maintainer = "mia <mia@mia.jetzt>"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "ac0d2371bf69d5136de7e9470c6fb286cbee2e16b4c7a6d2cd48a14796e86650"
hardening = ["cfi", "vis"]


# no tests, just make sure binary runs
def check(self):
    self.do("./build/btop", "--version")
