pkgname = "cpptrace"
pkgver = "1.0.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCPPTRACE_BUILD_SHARED=ON",
    "-DCPPTRACE_GET_SYMBOLS_WITH_LIBDWARF=ON",
    "-DCPPTRACE_USE_EXTERNAL_LIBDWARF=ON",
    "-DCPPTRACE_FIND_LIBDWARF_WITH_PKGCONFIG=ON",
    "-DCPPTRACE_USE_EXTERNAL_ZSTD=ON",
    "-DCPPTRACE_UNWIND_WITH_LIBUNWIND=ON",
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["libdwarf-devel", "libunwind-devel", "zstd-devel"]
pkgdesc = "Stacktrace library for C++11 and newer"
license = "MIT"
url = "https://github.com/jeremy-rifkin/cpptrace"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5c9f5b301e903714a4d01f1057b9543fa540f7bfcc5e3f8bd1748e652e24f9ea"


def post_install(self):
    self.install_license("LICENSE")


@subpackage("cpptrace-devel")
def _(self):
    return self.default_devel()
