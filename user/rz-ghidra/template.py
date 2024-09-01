pkgname = "rz-ghidra"
pkgver = "0.7.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    f"-DPROJECT_VERSION={pkgver}",
    "-DBUILD_CUTTER_PLUGIN=ON",
    "-DCUTTER_INSTALL_PLUGDIR=/usr/lib/cutter/plugins/native",
    "-DGENERATE_PARSERS=ON",
    "-DUSE_SYSTEM_PUGIXML=ON",
]
hostmakedepends = [
    "bison",
    "cmake",
    "flex",
    "ninja",
    "pkgconf",
]
makedepends = [
    "cutter-devel",
    "rizin-devel",
    "pugixml-devel",
]
pkgdesc = "Ghidra decompiler for Rizin"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-3.0-or-later"
url = "https://github.com/rizinorg/rz-ghidra"
source = f"{url}/releases/download/v{pkgver}/rz-ghidra-src-v{pkgver}.tar.gz"
sha256 = "62b9bc3e8f92efd7aa08a5fec710a19ef976c07f1dae9ba8f76539cc8b6fff6f"


@subpackage("rz-ghidra-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()
