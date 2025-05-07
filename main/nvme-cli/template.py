pkgname = "nvme-cli"
pkgver = "2.13"
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
sha256 = "43797e5b146ef5d4a67120fcdf38bb8254dcafefa714467d3f08dd675ebd40bb"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
