pkgname = "libnvme"
pkgver = "1.10"
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
source = f"{url}/archive/v{pkgver}/libnvme-v{pkgver}.tar.gz"
sha256 = "add9efa968e8341459fcaa2d96f2594a6f871e1fb3f57c02ce1c8ba5424f3960"


@subpackage("libnvme-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _(self):
    return self.default_devel()
