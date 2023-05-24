pkgname = "opencl-headers"
pkgver = "2023.04.17"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0ce992f4167f958f68a37918dec6325be18f848dee29a4521c633aae3304915d"
# no test suite
options = ["!check"]


def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
