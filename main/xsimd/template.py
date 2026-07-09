pkgname = "xsimd"
pkgver = "14.2.0"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cmake"
configure_args = ["-DBUILD_TESTS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["doctest"]
pkgdesc = "C++ wrappers for SIMD optimized mathematical functions"
license = "BSD-3-Clause"
url = "https://github.com/xtensor-stack/xsimd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "21e841ab684b05331e81e7f782431753a029ef7b7d9d6d3ddab837e7782a40ee"


if self.profile().cross:
    # cross compiling aarch64 tests gives error
    # error: unsupported argument 'native' to option '-mcpu='
    configure_args = ["-DBUILD_TESTS=OFF"]


match self.profile().arch:
    case "aarch64":
        # arm tests need sve
        configure_args = ["-DBUILD_TESTS=OFF"]


def post_install(self):
    self.install_license("LICENSE")
