pkgname = "libnvme"
pkgver = "1.5"
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
sha256 = "f73ba1edde059b2d5e7c1048ad4f895e6047bff241c94b34a7aff5894779d086"


@subpackage("libnvme-python")
def _py(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _devel(self):
    return self.default_devel()
