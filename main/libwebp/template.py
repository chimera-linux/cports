pkgname = "libwebp"
pkgver = "1.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "giflib-devel",
    "libpng-devel",
    "libtiff-devel",
    "freeglut-devel",
]
pkgdesc = "WebP image format library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://chromium.googlesource.com/webm/libwebp"
source = (
    f"http://downloads.webmproject.org/releases/webp/libwebp-{pkgver}.tar.gz"
)
sha256 = "7d6fab70cf844bf6769077bd5d7a74893f8ffd4dfb42861745750c63c2a5c92c"
tool_flags = {"CFLAGS": ["-DNDEBUG"]}
hardening = ["vis"]


def post_install(self):
    self.install_license("COPYING")
    self.install_dir("usr/lib/cmake")
    self.rename("usr/share/WebP/cmake", "usr/lib/cmake/WebP", relative=False)


@subpackage("libwebp-devel")
def _(self):
    self.depends += makedepends
    return self.default_devel()


@subpackage("libwebp-progs")
def _(self):
    return self.default_progs()
