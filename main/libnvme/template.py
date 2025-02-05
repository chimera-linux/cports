pkgname = "libnvme"
pkgver = "1.11.1"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/linux-nvme/libnvme"
source = f"{url}/archive/v{pkgver}/libnvme-v{pkgver}.tar.gz"
sha256 = "6d5d8ba2cc4c94a61a994c9f7f25b3b26ef973fb5c0daa37729890903f37a1f1"


@subpackage("libnvme-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _(self):
    return self.default_devel()
