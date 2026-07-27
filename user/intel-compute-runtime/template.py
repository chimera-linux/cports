pkgname = "intel-compute-runtime"
pkgver = "26.27.39122.11"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DCMAKE_INSTALL_LIBDIR=lib",
    "-DDISABLE_WDDM_LINUX=ON",
    "-DNEO_DISABLE_LD_GOLD=ON",
    "-DNEO_SKIP_UNIT_TESTS=ON",
    "-DNEO_DISABLE_LTO=ON",
    "-DNEO_BUILD_UNVERSIONED_OCLOC=ON",
    "-DIGC_DIR=/usr",
]
hostmakedepends = [
    "clang",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "igsc-devel",
    "intel-gmmlib-devel",
    "intel-graphics-compiler-devel",
    "level-zero-headers",
    "libdrm-devel",
    "libva-devel",
    "opencl-headers",
    "udev-devel",
]
depends = [
    "intel-gmmlib",
    "intel-graphics-compiler",
]
pkgdesc = "Intel oneAPI Level Zero and OpenCL compute runtime"
license = "MIT"
url = "https://github.com/intel/compute-runtime"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "914f5626d0067881f0a390d9f05a165230f47e36126728e3d6f4ce2b7fef946c"
# disabled test suite
options = ["!check", "etcfiles"]

# upstream forces _FORTIFY_SOURCE=2
# fix runtime error in blender
tool_flags = {
    "CFLAGS": [
        "-Wno-error=macro-redefined",
        "-DSANITIZER_BUILD=1",
    ],
    "CXXFLAGS": [
        "-Wno-error=macro-redefined",
        "-DSANITIZER_BUILD=1",
    ],
}


def post_install(self):
    self.install_license("LICENSE.md")


@subpackage("intel-compute-runtime-devel")
def _(self):
    self.subdesc = "headers"
    self.depends = ["level-zero-headers"]

    return ["usr/include"]
