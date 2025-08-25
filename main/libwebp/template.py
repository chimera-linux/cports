pkgname = "libwebp"
pkgver = "1.6.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "freeglut-devel",
    "giflib-devel",
    "libpng-devel",
    "libtiff-devel",
]
pkgdesc = "WebP image format library"
license = "BSD-3-Clause"
url = "https://chromium.googlesource.com/webm/libwebp"
source = (
    f"http://downloads.webmproject.org/releases/webp/libwebp-{pkgver}.tar.gz"
)
sha256 = "e4ab7009bf0629fd11982d4c2aa83964cf244cffba7347ecd39019a9e38c4564"
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
