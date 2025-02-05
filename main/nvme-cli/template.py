pkgname = "nvme-cli"
pkgver = "2.11"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://github.com/linux-nvme/nvme-cli"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5e4dc73dbb488c6b1e6ad1c78d0c62b624076fcb0c052bd9039674a1dbd6517b"
hardening = ["vis", "cfi"]
# require /dev nvme device
options = ["!check"]


def post_install(self):
    self.uninstall("usr/lib/systemd/system")
