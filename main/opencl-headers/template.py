pkgname = "opencl-headers"
pkgver = "2024.05.08"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3c3dd236d35f4960028f4f58ce8d963fb63f3d50251d1e9854b76f1caab9a309"
# no test suite
options = ["!check"]


def install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
