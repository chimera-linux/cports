pkgname = "nvme-cli"
pkgver = "2.7"
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
sha256 = "bc06c1d7da991d39a1397a3506d760aa1dc3ba0741ebbf4b5bf5222625f6624f"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]
