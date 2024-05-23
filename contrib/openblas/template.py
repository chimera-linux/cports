pkgname = "openblas"
pkgver = "0.3.27"
pkgrel = 0
archs = ["aarch64", "ppc", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON", "-DUSE_OPENMP=1"]
# FIXME: flang support
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libomp-devel", "linux-headers"]
pkgdesc = "Optimized BLAS library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://www.openblas.net"
source = f"https://github.com/OpenMathLib/OpenBLAS/releases/download/v{pkgver}/OpenBLAS-{pkgver}.tar.gz"
sha256 = "aa2d68b1564fe2b13bc292672608e9cdeeeb6dc34995512e65c3b10f4599e897"

match self.profile().arch:
    case "aarch64":
        configure_args += ["-DTARGET=ARMV8"]
    case "ppc":
        configure_args += ["-DTARGET=PPCG4"]
    case "ppc64":
        configure_args += ["-DTARGET=PPC970MP"]
    case "ppc64le":
        configure_args += ["-DTARGET=POWER8"]
    case "riscv64":
        configure_args += ["-DTARGET=RISCV64_GENERIC"]
    case "x86_64":
        configure_args += ["-DTARGET=GENERIC"]

if self.profile().arch in ["aarch64", "ppc64le", "riscv", "x86_64"]:
    configure_args += ["-DDYNAMIC_ARCH=ON"]

if self.profile().arch in ["ppc", "ppc64", "ppc64le"]:
    # needs GNU as
    hostmakedepends += [f"binutils-{self.profile().arch}"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openblas-devel")
def _devel(self):
    return self.default_devel()
