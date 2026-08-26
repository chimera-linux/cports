pkgname = "nvme-cli"
pkgver = "2.16"
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
    "linux-headers",
    "util-linux-uuid-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "NVMe management command line interface"
license = "GPL-2.0-or-later"
url = "https://github.com/linux-nvme/nvme-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "989682ed7b250a2c7a8127e362ffc5d29f5c370127abe405be09c73216da2b97"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["etcfiles", "!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
