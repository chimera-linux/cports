pkgname = "swayimg"
pkgver = "4.2"
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
    "libraw-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "openexr-devel",
    "wayland-devel",
]
pkgdesc = "Image viewer for sway/wayland"
license = "MIT"
url = "https://github.com/artemsen/swayimg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1e4fa2027a91df86790a77449efe3515bbacc0564a85f980fc8631a30d5f242e"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
