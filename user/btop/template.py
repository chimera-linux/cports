pkgname = "btop"
pkgver = "1.4.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "40f6c54d1bc952c674b677d81dd25f55b61e9c004883c27950dc30780c86f381"
hardening = ["cfi", "vis"]


# no tests, just make sure binary runs
def check(self):
    self.do("./build/btop", "--version")
