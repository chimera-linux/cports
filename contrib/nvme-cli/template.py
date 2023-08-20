pkgname = "nvme-cli"
pkgver = "2.5"
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
sha256 = "e84bdba276aadcddda8cf5d412e934cc5673af15132ea02180deb5d06af73146"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]
