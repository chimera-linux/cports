pkgname = "btop"
pkgver = "1.4.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "0ffe03d3e26a3e9bbfd5375adf34934137757994f297d6b699a46edd43c3fc02"
hardening = ["cfi", "vis"]


# no tests, just make sure binary runs
def check(self):
    self.do("./build/btop", "--version")
