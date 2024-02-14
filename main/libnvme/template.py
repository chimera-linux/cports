pkgname = "libnvme"
pkgver = "1.8"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf", "bash", "swig"]
makedepends = [
    "dbus-devel",
    "json-c-devel",
    "keyutils-devel",
    "linux-headers",
    "openssl-devel",
    "python-devel",
]
pkgdesc = "C library for NVMe on Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/linux-nvme/libnvme"
source = f"{url}/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "d59939a280eec41eb7a716e1681d0d0c612099385204ffb55d07134a6be08d75"
options = ["linkundefver"]


@subpackage("libnvme-python")
def _py(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _devel(self):
    return self.default_devel()
