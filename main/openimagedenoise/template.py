pkgname = "openimagedenoise"
pkgver = "2.3.2"
pkgrel = 0
# ispc
archs = ["x86_64", "aarch64", "armv7"]
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "ispc",
    "ninja",
    "python",
]
makedepends = [
    "onetbb-devel",
    "ispc-devel",
]
pkgdesc = "Ray-tracing denoising library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://www.openimagedenoise.org"
source = f"https://github.com/RenderKit/oidn/releases/download/v{pkgver}/oidn-{pkgver}.src.tar.gz"
sha256 = "0ca50e621294e8be238bee2d814fb0391e252e3f3c93fdd4bc253a60e0d00c68"
# set in release
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# guilty until proven innocent
hardening = ["!int"]


@subpackage("openimagedenoise-progs")
def _(self):
    return self.default_progs()


@subpackage("openimagedenoise-devel")
def _(self):
    return self.default_devel()
