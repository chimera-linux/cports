pkgname = "libplacebo"
pkgver = "7.351.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dshaderc=enabled",
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
    "lcms2-devel",
    "libdovi-devel",
    "mesa-devel",
    "shaderc-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "xxhash-devel",
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
_fast_float = "v6.1.0"
source = [
    f"{url}/-/archive/v{pkgver}/libplacebo-v{pkgver}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/{_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "3rdparty/fast_float",
]
sha256 = [
    "4efe1c8d4da3c61295eb5fdfa50e6037409d8425eb3c15dd86788679c4ce59ee",
    "5a629e1f18f037ad0016c41ead630ea471cccbcdf60239ed3466c491d8e7c908",
]
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _(self):
    return self.default_devel()
