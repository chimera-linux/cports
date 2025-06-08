pkgname = "qdiskinfo"
pkgver = "0.4"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-devel"]
depends = [
    "qt6-qtsvg",
    "smartmontools",
]
pkgdesc = "Frontend for smartctl to display SMART data"
license = "GPL-3.0-only"
url = "https://github.com/edisionnano/QDiskInfo"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "33762f494f2da4b59e770207ad5bacca4394774c76509c15d3e3fa23fbf76d33"
