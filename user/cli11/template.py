pkgname = "cli11"
pkgver = "2.7.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCLI11_BUILD_EXAMPLES=OFF",
    "-DCLI11_BUILD_TESTS=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
checkdepends = ["catch2-devel"]
pkgdesc = "Command line parser for C++11"
license = "BSD-3-Clause"
url = "https://github.com/CLIUtils/CLI11"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "46eef3101da70852ec7af026e09d485ccee81813331c8c6052d39344443b83da"
tool_flags = {"CXXFLAGS": ["-Wno-c2y-extensions"]}

if self.profile().cross:
    # checkdepends aren't installed at configure time; CLI11 falls back to
    # downloading a legacy Catch header, no network in cross.
    configure_args += ["-DCLI11_BUILD_TESTS=OFF"]


def post_install(self):
    self.install_license("LICENSE")
