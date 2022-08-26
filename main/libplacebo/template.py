pkgname = "libplacebo"
pkgver = "4.208.0"
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
sha256 = "7b3c857934ee3d30f743e43d7f0606e10950806661ea0ea385f8a1f06cbab854"

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
