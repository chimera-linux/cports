pkgname = "swayimg"
pkgver = "1.12"
pkgrel = 1
build_style = "meson"
hostmakedepends = [
    "bash-completion",
    "meson",
    "pkgconf",
    "wayland-protocols",
]
makedepends = [
    "fontconfig-devel",
    "json-c-devel",
    "libexif-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "libpng-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "wayland-devel",
]
pkgdesc = "Image viewer for sway/wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/artemsen/swayimg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4617322a1ec17985770dc351eea69b42b1464f2d838eb5015314634b2a30f126"


def post_install(self):
    self.install_license("LICENSE")
