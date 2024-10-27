pkgname = "imv"
pkgver = "4.5.0"
pkgrel = 2
build_style = "meson"
configure_args = [
    "-Dfreeimage=disabled",
    "-Dlibjpeg=enabled",
    "-Dlibjxl=enabled",
    "-Dlibnsgif=disabled",
    "-Dlibpng=enabled",
    "-Dlibtiff=enabled",
    "-Dman=enabled",
    "-Dtest=enabled",
    "-Dunicode=icu",
    "-Dwindows=all",
]
hostmakedepends = [
    "asciidoc",
    "meson",
    "pkgconf",
]
makedepends = [
    "cmocka-devel",
    "glu-devel",
    "icu-devel",
    "inih-devel",
    "libheif-devel",
    "libjpeg-turbo-devel",
    "libjxl-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "pango-devel",
    "wayland-devel",
]
pkgdesc = "Image viewer for X11/Wayland"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://sr.ht/~exec64/imv"
source = f"https://git.sr.ht/~exec64/imv/archive/v{pkgver}.tar.gz"
sha256 = "3b11991a86942d757830015033b1c3a3cc915be2f0c20fee7bc7493be560cbcb"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
