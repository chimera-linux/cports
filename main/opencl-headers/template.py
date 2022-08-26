pkgname = "opencl-headers"
pkgver = "2022.05.18"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "88a1177853b279eaf574e2aafad26a84be1a6f615ab1b00c20d5af2ace95c42e"
# no test suite
options = ["!check"]

def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
