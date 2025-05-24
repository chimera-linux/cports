pkgname = "btop"
pkgver = "1.4.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "81b133e59699a7fd89c5c54806e16452232f6452be9c14b3a634122e3ebed592"
hardening = ["cfi", "vis"]


# no tests, just make sure binary runs
def check(self):
    self.do("./build/btop", "--version")
