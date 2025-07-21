pkgname = "openimagedenoise"
pkgver = "2.3.3"
pkgrel = 1
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ispc",
    "ninja",
    "python",
]
makedepends = [
    "ispc-devel",
    "onetbb-devel",
]
pkgdesc = "Ray-tracing denoising library"
license = "Apache-2.0"
url = "https://www.openimagedenoise.org"
source = f"https://github.com/RenderKit/oidn/releases/download/v{pkgver}/oidn-{pkgver}.src.tar.gz"
sha256 = "ccf221535b4007607fb53d3ff5afa74de25413bb8ef5d03d215f46c7cc2f96cf"
# set in release
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# guilty until proven innocent
hardening = ["!int"]

if self.profile().wordsize == 32:
    broken = "supports 64-bit only"


@subpackage("openimagedenoise-progs")
def _(self):
    return self.default_progs()


@subpackage("openimagedenoise-devel")
def _(self):
    return self.default_devel()
