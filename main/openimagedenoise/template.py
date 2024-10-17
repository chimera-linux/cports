pkgname = "openimagedenoise"
pkgver = "2.3.0"
pkgrel = 2
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
sha256 = "cce3010962ec84e0ba1acd8c9055a3d8de402fedb1b463517cfeb920a276e427"
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
