pkgname = "opencl-headers"
pkgver = "2025.06.13"
pkgrel = 0
pkgdesc = "OpenCL header files"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "8bf2fda271c3511ee1cd9780b97446e9fa0cf2b0765cdd54aee60074a4567644"
# no test suite
options = ["!check"]


def install(self):
    self.install_file("CL/*.h", "usr/include/CL", glob=True)
