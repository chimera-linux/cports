pkgname = "nvme-cli"
pkgver = "2.7.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "bash",
    "meson",
    "ninja",
    "pkgconf",
]
makedepends = [
    "libnvme-devel",
    "libuuid-devel",
    "linux-headers",
    "zlib-devel",
]
pkgdesc = "NVMe management command line interface"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/linux-nvme/nvme-cli"
source = (
    f"https://github.com/linux-nvme/nvme-cli/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "4c69d0f3c8b553110d0f63f5876d56627abd2d9f5d3904e2480cedd03cb15654"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]
