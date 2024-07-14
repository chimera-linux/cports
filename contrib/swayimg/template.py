pkgname = "swayimg"
pkgver = "2.4"
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
sha256 = "6a9df60600764daccbe7b3015b51e1ac08d4cdf7afa8cd65b8cd8c06943f5f83"


def post_install(self):
    self.install_license("LICENSE")
