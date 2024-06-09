pkgname = "libnvme"
pkgver = "1.9"
pkgrel = 1
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
sha256 = "455867060d2b7563eab59fe21779dff469d98465028997178c7efbe4b8763206"
options = ["linkundefver"]


@subpackage("libnvme-python")
def _py(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]


@subpackage("libnvme-devel")
def _devel(self):
    return self.default_devel()
