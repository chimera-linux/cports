pkgname = "opencl-headers"
pkgver = "2023.02.06"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "464d1b04a5e185739065b2d86e4cebf02c154c416d63e6067a5060d7c053c79a"
# no test suite
options = ["!check"]

def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
