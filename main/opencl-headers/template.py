pkgname = "opencl-headers"
pkgver = "2023.12.14"
pkgrel = 0
pkgdesc = "OpenCL header files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Apache-2.0"
url = "https://github.com/KhronosGroup/OpenCL-Headers"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "407d5e109a70ec1b6cd3380ce357c21e3d3651a91caae6d0d8e1719c69a1791d"
# no test suite
options = ["!check"]


def do_install(self):
    for f in (self.cwd / "CL").glob("*.h"):
        self.install_file(f, "usr/include/CL")
