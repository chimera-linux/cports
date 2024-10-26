pkgname = "opencl-headers"
pkgver = "2024.10.24"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "159f2a550592bae49859fee83d372acd152328fdf95c0dcd8b9409f8fad5db93"
# no test suite
options = ["!check"]


def install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
