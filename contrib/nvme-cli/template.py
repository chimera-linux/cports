pkgname = "nvme-cli"
pkgver = "2.8"
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
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0743d9188792a87d39187ae5e5cb31e8f46cca8c6f100547c50ec0dd659d2531"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]
