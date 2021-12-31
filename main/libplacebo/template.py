pkgname = "libplacebo"
pkgver = "4.157.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dshaderc=enabled", "-Dvulkan=enabled",
    "-Dopengl=enabled", "-Dlcms=enabled",
]
hostmakedepends = [
    "meson", "pkgconf", "python-mako", "vulkan-headers"
]
makedepends = [
    "shaderc-devel", "vulkan-headers", "vulkan-loader",
    "lcms2-devel", "libepoxy-devel"
]
pkgdesc = "Reusable library for GPU-accelerated video/image rendering"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://code.videolan.org/videolan/libplacebo"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "8ee7773fb7813520b6b1e5f8f207cdf0071a7cf48ca0ce871e956ae6f4d0d538"

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
