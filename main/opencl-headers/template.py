pkgname = "opencl-headers"
pkgver = "2022.09.30"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "0ae857ecb28af95a420c800b21ed2d0f437503e104f841ab8db249df5f4fbe5c"
# no test suite
options = ["!check"]

def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
