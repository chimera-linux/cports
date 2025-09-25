pkgname = "cli11"
pkgver = "2.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCLI11_SINGLE_FILE=OFF",  # Build the CLI11.hpp file from the sources. Requires Python (version 3 or 2.7).
    "-DCLI11_PRECOMPILED=OFF",  # generate a precompiled static library instead of header-only
    "-DCLI11_SINGLE_FILE_TESTS=OFF",  # Run the tests on the generated single file version as well
    "-DCLI11_BUILD_DOCS=ON",  # build CLI11 documentation and book
    "-DCLI11_BUILD_EXAMPLES=OFF",  # Build the example programs.
    "-DCLI11_BUILD_EXAMPLES_JSON=OFF",  # Build some additional example using json libraries
    "-DCLI11_INSTALL=ON",  # install CLI11 to the install folder during the install process
    "-DCLI11_FORCE_LIBCXX=OFF",  # use libc++ instead of libstdc++ if building with clang on linux
    "-DCLI11_CUDA_TESTS=OFF",  # build the tests with NVCC
    "-DCLI11_BUILD_TESTS=ON",  # Build the tests.
]
hostmakedepends = ["boost", "cmake", "doxygen", "ninja", "pkgconf", "python"]
makedepends = ["catch2-devel"]
pkgdesc = "Command line parser for C++11 and beyond"
license = "custom:cli11"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "17e02b4cddc2fa348e5dbdbb582c59a3486fa2b2433e70a0c3bacb871334fd55"


def post_install(self):
    self.install_license("LICENSE")
