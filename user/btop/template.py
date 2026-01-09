pkgname = "btop"
pkgver = "1.4.6"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBTOP_LTO=OFF", "-DBTOP_FORTIFY=OFF"]
hostmakedepends = ["cmake", "ninja", "lowdown"]
makedepends = ["linux-headers"]
checkdepends = ["gtest-devel"]
pkgdesc = "TUI monitor of system resources"
license = "Apache-2.0"
url = "https://github.com/aristocratos/btop"
source = f"{url}/archive/v{pkgver}/btop-{pkgver}.tar.gz"
sha256 = "4beb90172c6acaac08c1b4a5112fb616772e214a7ef992bcbd461453295a58be"
hardening = ["cfi", "vis"]
