pkgname = "libplacebo"
pkgver = "6.338.1"
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
    "vulkan-loader-devel",
    "lcms2-devel",
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
_fast_float = "v5.2.0"
source = [
    f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/{_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "3rdparty/fast_float",
]
sha256 = [
    "f748bf9385f4c228e1379d7d1bed13581176bfdc54eb99f4abe22e649f8dc93f",
    "72bbfd1914e414c920e39abdc81378adf910a622b62c45b4c61d344039425d18",
]
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
