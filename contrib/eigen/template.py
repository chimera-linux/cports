pkgname = "eigen"
pkgver = "3.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["boost-devel", "mpfr-devel", "fftw-devel"]
pkgdesc = "C++ template library for linear algebra"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MPL-2.0"
url = "https://eigen.tuxfamily.org"
source = f"https://gitlab.com/libeigen/eigen/-/archive/{pkgver}/eigen-{pkgver}.tar.bz2"
sha256 = "b4c198460eba6f28d34894e3a5710998818515104d6e74e5cc331ce31e46e626"
# too many tests say "not run"
options = ["!check"]
