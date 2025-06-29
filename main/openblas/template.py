pkgname = "openblas"
pkgver = "0.3.30"
pkgrel = 0
archs = [
    "aarch64",
    "loongarch64",
    "ppc",
    "ppc64",
    "ppc64le",
    "riscv64",
    "x86_64",
]
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    f"-DBINARY={self.profile().wordsize}",
]
# FIXME: flang support
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["linux-headers"]
pkgdesc = "Optimized BLAS library"
license = "BSD-3-Clause"
url = "https://www.openblas.net"
source = f"https://github.com/OpenMathLib/OpenBLAS/releases/download/v{pkgver}/OpenBLAS-{pkgver}.tar.gz"
sha256 = "27342cff518646afb4c2b976d809102e368957974c250a25ccc965e53063c95d"

_have_omp = True

match self.profile().arch:
    case "aarch64":
        configure_args += ["-DTARGET=ARMV8"]
    case "loongarch64":
        configure_args += ["-DTARGET=LA64_GENERIC"]
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

# riscv64/loongarch64 dynamic_arch is currently broken
if self.profile().arch in ["aarch64", "ppc64le", "x86_64"]:
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
