pkgname = "swayimg"
pkgver = "5.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    f"-Dversion={pkgver}",
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
    "gtest-devel",
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
    "luajit-devel",
    "openexr-devel",
    "wayland-devel",
]
checkdepends = ["fonts-liberation-otf"]
pkgdesc = "Image viewer for sway/wayland"
license = "MIT"
url = "https://github.com/artemsen/swayimg"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0f70cbc665217a747e8a098e1a881239e96df270930f47c262ab2ecff290e428"
