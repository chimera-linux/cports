pkgname = "libplacebo"
pkgver = "4.192.1"
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
sha256 = "e6c5805cf4d955b5941dd12b00fe157b61e77995bc1786b9a86df0ca99a0edc4"

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
