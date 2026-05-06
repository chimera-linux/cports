pkgname = "libplacebo"
pkgver = "7.360.1"
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
_fast_float = "v8.0.2"
source = [
    f"{url}/-/archive/v{pkgver}/libplacebo-v{pkgver}.tar.gz",
    f"https://github.com/fastfloat/fast_float/archive/{_fast_float}.tar.gz",
]
source_paths = [
    ".",
    "3rdparty/fast_float",
]
sha256 = [
    "14c0a99f4b01557ec9826ce6b1d52f6de21be274ba03fd5aab7307f18766dc39",
    "e14a33089712b681d74d94e2a11362643bd7d769ae8f7e7caefe955f57f7eacd",
]
hardening = ["vis", "!cfi"]


@subpackage("libplacebo-devel")
def _(self):
    return self.default_devel()
