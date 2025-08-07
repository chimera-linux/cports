pkgname = "nvme-cli"
pkgver = "2.15"
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
sha256 = "93282c426f22dd1ea6d172dec8af043c4e9ff80189becfbbb5378fe1ca0a74ad"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
