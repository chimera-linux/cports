pkgname = "libplacebo"
pkgver = "6.292.1"
pkgrel = 2
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
sha256 = "3f25b32b37f24b2247f5024e8db252e617cb368c3f25e04b3f50d6355009754f"
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
