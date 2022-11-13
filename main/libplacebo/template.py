pkgname = "libplacebo"
pkgver = "5.229.1"
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
sha256 = "fc021fc68376b92511977b5bd32340fc575dc36af5c471cc095b5b7e3fa581d4"

@subpackage("libplacebo-devel")
def _devel(self):
    return self.default_devel()
