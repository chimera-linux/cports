pkgname = "swayimg"
pkgver = "3.7"
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
    "openexr-devel",
    "wayland-devel",
]
pkgdesc = "Image viewer for sway/wayland"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/artemsen/swayimg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "967a335cc2e62b155f0523a2a9e7592f076a5eec4828fcc6306ae165d19b8a96"


def post_install(self):
    self.install_license("LICENSE")
