pkgname = "libplacebo"
pkgver = "6.338.2"
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
    "python-glad",
    "python-jinja2",
    "python-markupsafe",
    "vulkan-headers",
]
makedepends = [
    "glslang-devel",
    "lcms2-devel",
    "mesa-devel",
    "shaderc-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
_fast_float = "v6.1.0"
source = [
    f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/{_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "3rdparty/fast_float",
]
sha256 = [
    "d029adbe55bba8aed7aed2c48b0b66081dddfb9d42683a709342e33aa666c544",
    "a9c8ca8ca7d68c2dbb134434044f9c66cfd4c383d5e85c36b704d30f6be82506",
]
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
