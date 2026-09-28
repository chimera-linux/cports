pkgname = "libiio"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DWITH_ZSTD=ON",
    "-DUDEV_RULES_INSTALL_DIR=/usr/lib/udev/rules.d",
]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "pkgconf",
]
makedepends = [
    "avahi-devel",
    "dinit-chimera",
    "libaio-devel",
    "libusb-devel",
    "libxml2-devel",
    "linux-headers",
    "zstd-devel",
]
pkgdesc = "Library for Linux IIO devices"
license = "LGPL-2.1-or-later"
url = "https://github.com/analogdevicesinc/libiio"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b4289bf9971f4a193c8c5f7fb40fbd4bd3f33654936b960b9539c7f2b484e44a"


def post_install(self):
    self.install_file(self.files_path / "iiod.wrapper", "usr/lib", mode=0o755)
    self.install_service(self.files_path / "iiod")


@subpackage("libiio-progs")
def _(self):
    return self.default_progs(extra=["usr/lib/iiod.wrapper", "usr/lib/dinit.d"])


@subpackage("libiio-devel")
def _(self):
    return self.default_devel()
