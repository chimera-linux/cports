pkgname = "nvme-cli"
pkgver = "2.9.1"
pkgrel = 1
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
    "zlib-ng-compat-devel",
]
pkgdesc = "NVMe management command line interface"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/linux-nvme/nvme-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4b61684a1d23de1d9d0abd3f273799c60256c0e2a2e68a790d7945183fe33874"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
