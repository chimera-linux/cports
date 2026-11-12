pkgname = "swayimg"
pkgver = "5.7"
pkgrel = 0
build_style = "meson"
configure_args = [
    f"-Dversion={pkgver}",
    "-Dliblua=lua",
    "-Dtests=enabled",
    "-Dvideo=disabled",
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
    "lua5.4-devel",
    "openexr-devel",
    "wayland-devel",
]
checkdepends = ["gtest-devel", "fonts-liberation-otf"]
pkgdesc = "Image viewer for sway/wayland"
license = "MIT"
url = "https://github.com/artemsen/swayimg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "22e602cba022972ccc6e9701827135282679a5a8efc818132fdf56ce40a7d6fa"
hardening = ["vis", "!cfi", "!int"]
