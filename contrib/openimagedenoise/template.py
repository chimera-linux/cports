pkgname = "openimagedenoise"
pkgver = "2.2.2"
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
source = f"https://github.com/OpenImageDenoise/oidn/releases/download/v{pkgver}/oidn-{pkgver}.src.tar.gz"
sha256 = "d26b75fa216165086f65bf48c80648290f2cfed7d3c4bfc1e86c247b46c96b7e"
# set in release
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# guilty until proven innocent
hardening = ["!int"]


@subpackage("openimagedenoise-progs")
def _progs(self):
    return self.default_progs()


@subpackage("openimagedenoise-devel")
def _devel(self):
    return self.default_devel()
