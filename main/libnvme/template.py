pkgname = "libnvme"
pkgver = "1.15"
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
sha256 = "c21cd9379390bdc52c9d9569a241274f8115fc247b76a5d922d639f48c8174a2"


@subpackage("libnvme-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _(self):
    return self.default_devel()
