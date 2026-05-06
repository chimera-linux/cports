pkgname = "openimagedenoise"
pkgver = "2.4.1"
pkgrel = 0
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
sha256 = "9c7c77ae0d57e004479cddb7aaafd405c2cc745153bed4805413c21be610e17b"
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
