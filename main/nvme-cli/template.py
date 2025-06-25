pkgname = "nvme-cli"
pkgver = "2.14"
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
sha256 = "ff689ec0dabd32e8077a9fc0b2732067b08dedeef471aadea0136ae210f6edd1"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
