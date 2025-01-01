pkgname = "openblas"
pkgver = "0.3.28"
pkgrel = 0
archs = ["aarch64", "ppc", "ppc64", "ppc64le", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    f"-DBINARY={self.profile().wordsize}",
]
# FIXME: flang support
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Optimized BLAS library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://www.openblas.net"
source = f"https://github.com/OpenMathLib/OpenBLAS/releases/download/v{pkgver}/OpenBLAS-{pkgver}.tar.gz"
sha256 = "f1003466ad074e9b0c8d421a204121100b0751c96fc6fcf3d1456bd12f8a00a1"

_have_omp = True

match self.profile().arch:
    case "aarch64":
        configure_args += ["-DTARGET=ARMV8"]
    case "ppc":
        configure_args += ["-DTARGET=PPCG4"]
        _have_omp = False
    case "ppc64":
        configure_args += ["-DTARGET=PPC970MP"]
    case "ppc64le":
        configure_args += ["-DTARGET=POWER8"]
    case "riscv64":
        configure_args += ["-DTARGET=RISCV64_GENERIC"]
    case "x86_64":
        configure_args += ["-DTARGET=GENERIC"]

if self.profile().arch in ["aarch64", "ppc64le", "riscv64", "x86_64"]:
    configure_args += ["-DDYNAMIC_ARCH=ON"]

if self.profile().arch in ["ppc", "ppc64", "ppc64le"]:
    # needs GNU as
    hostmakedepends += [f"binutils-{self.profile().arch}"]

if _have_omp:
    makedepends += ["libomp-devel"]
    configure_args += ["-DUSE_OPENMP=1"]


def post_install(self):
    self.install_license("LICENSE")


@subpackage("openblas-devel")
def _(self):
    return self.default_devel()
