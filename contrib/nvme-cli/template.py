pkgname = "nvme-cli"
pkgver = "2.6"
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
sha256 = "7e2f11eb7a9c1b9343d537a32ae5c78f51de20cd4a6cdddb2bc2459c259b33d6"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]
