pkgname = "libplacebo"
pkgver = "5.264.0"
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
sha256 = "d8e2d732fdff10a73f3aee93131f9a529ae3f71a6b9c0d6e1634d071c7f6a6b2"
# FIXME cfi
hardening = ["vis", "!cfi"]

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
