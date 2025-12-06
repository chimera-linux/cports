pkgname = "cli11"
pkgver = "2.6.1"
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
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["catch2-devel"]
pkgdesc = "Command line parser for C++11 and beyond"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "377691f3fac2b340f12a2f79f523c780564578ba3d6eaf5238e9f35895d5ba95"


def post_install(self):
    self.install_license("LICENSE")
