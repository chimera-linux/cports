pkgname = "libnvme"
pkgver = "1.7.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf", "bash", "swig"]
makedepends = [
    "json-c-devel",
    "openssl-devel",
    "dbus-devel",
    "python-devel",
    "keyutils-devel",
    "linux-headers",
]
pkgdesc = "C library for NVMe on Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/linux-nvme/libnvme"
source = f"{url}/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "e9c3ad59c068788faf0f0af4296f92f8ce410d12749f0f35a541d6a21e630393"
options = ["linkundefver"]


@subpackage("libnvme-python")
def _py(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _devel(self):
    return self.default_devel()
