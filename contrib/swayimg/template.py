pkgname = "swayimg"
pkgver = "2.3"
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
sha256 = "c5bde4bee699d8379cd666a027db806fdc3dc08639fd53edbc2fcf8cffab038d"


def post_install(self):
    self.install_license("LICENSE")
