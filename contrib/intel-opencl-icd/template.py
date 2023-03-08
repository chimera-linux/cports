pkgname = "intel-opencl-icd"
pkgver = "22.53.25242.13"
pkgrel = 0
build_style = "cmake"
# some illegal casts, maybe we can patch the casts?
# sounds like a lot of work for rather no or small value right now
configure_args = ["-DSKIP_UNIT_TESTS=1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["gmmlib-devel", "intel-graphics-compiler-devel", "libexecinfo-devel", "linux-headers"]
pkgdesc = "Intel® Graphics Compute Runtime for oneAPI Level Zero and OpenCL™ Driver"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://foo.software"
source = f"https://github.com/intel/compute-runtime/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "09d7e119c4b442677307a86d257f0e65d27bb86b5fa55669f5603db3e1f041c2"
# no tests
options = ["!check"]
