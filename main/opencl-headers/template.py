pkgname = "opencl-headers"
pkgver = "2022.01.04"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6e716e2b13fc8d363b40a165ca75021b102f9328e2b38f8054d7db5884de29c9"
# no test suite
options = ["!check"]

def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
