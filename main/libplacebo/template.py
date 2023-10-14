pkgname = "libplacebo"
pkgver = "6.338.0"
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
    "bd1a93ba89905af8f9c09ddfe0426f5277dbc0459d543c72cff49e7d50b0d5b2",
    "72bbfd1914e414c920e39abdc81378adf910a622b62c45b4c61d344039425d18",
]
# FIXME cfi
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
