pkgname = "swayimg"
pkgver = "2.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    f"-Dversion={pkgver}",
    "-Dzsh=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "wayland-protocols",
]
makedepends = [
    "bash-completion",
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
sha256 = "51d18c0c8229b1cf25c1a221a12fc8e11a9b4f7da0cef79bcfa434fdcf3d7213"


def post_install(self):
    self.install_license("LICENSE")
