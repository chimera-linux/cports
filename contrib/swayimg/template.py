pkgname = "swayimg"
pkgver = "2.0"
pkgrel = 0
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
    "libavif-devel",
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
sha256 = "afcf69d9c69d826e010065dd08732fc5b0c0402c26f98d977f27b77ebd2bdee1"


def post_install(self):
    self.install_license("LICENSE")
