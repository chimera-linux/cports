pkgname = "libplacebo"
pkgver = "6.292.0"
pkgrel = 1
build_style = "meson"
configure_args = [
    "-Dshaderc=enabled",
    "-Dglslang=enabled",
    "-Dvulkan=enabled",
    "-Dopengl=enabled",
    "-Dlcms=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-jinja2",
    "python-glad",
    "python-markupsafe",
    "vulkan-headers",
]
makedepends = [
    "shaderc-devel",
    "glslang-devel",
    "vulkan-headers",
    "vulkan-loader",
    "lcms2-devel",
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "22116cfada2a878407c1da8f60d4b7497137f7fcb625f90e8669422cae8749f0"
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
