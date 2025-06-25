pkgname = "libnvme"
pkgver = "1.14"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddocs=false"]
hostmakedepends = ["meson", "pkgconf", "bash", "swig"]
makedepends = [
    "dbus-devel",
    "json-c-devel",
    "keyutils-devel",
    "linux-headers",
    "openssl3-devel",
    "python-devel",
]
pkgdesc = "C library for NVMe on Linux"
license = "LGPL-2.1-or-later"
url = "https://github.com/linux-nvme/libnvme"
source = f"{url}/archive/v{pkgver}/libnvme-v{pkgver}.tar.gz"
sha256 = "a7230d6d4959f26cf0c0ef6c9bb479bd94a8c0ec738bf6e164d66c3dc6397e66"


@subpackage("libnvme-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _(self):
    return self.default_devel()
