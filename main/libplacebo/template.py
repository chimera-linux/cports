pkgname = "libplacebo"
pkgver = "5.264.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dshaderc=enabled", "-Dglslang=enabled", "-Dvulkan=enabled",
    "-Dopengl=enabled", "-Dlcms=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "python-jinja2", "python-glad", "python-markupsafe",
    "vulkan-headers"
]
makedepends = [
    "shaderc-devel", "glslang-devel", "vulkan-headers", "vulkan-loader",
    "lcms2-devel",
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "9eb0c198f58d994f1c0d173dd37647d4d07d27972412c48ab758e984503c787b"
# FIXME cfi
hardening = ["vis", "!cfi"]

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
