pkgname = "swayimg"
pkgver = "2.1"
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
sha256 = "d82fb8e75cdabf470677797444ec19b00c83e0e06d80be774727194404624e7e"


def post_install(self):
    self.install_license("LICENSE")
