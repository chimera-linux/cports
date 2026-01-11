pkgname = "imv"
pkgver = "5.0.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dlibjpeg=enabled",
    "-Dlibjxl=enabled",
    "-Dlibnsgif=disabled",
    "-Dlibpng=enabled",
    "-Dlibtiff=enabled",
    "-Dlibwebp=enabled",
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
    "wayland-protocols",
]
checkdepends = ["vim-xxd"]
pkgdesc = "Image viewer for X11/Wayland"
license = "MIT"
url = "https://sr.ht/~exec64/imv"
source = f"https://git.sr.ht/~exec64/imv/archive/v{pkgver}.tar.gz"
sha256 = "8949c1df4b933b1d324e02ce49f1834a4b73dd25fa8103579e0ed105149e080e"
# cfi: sigill when opening images
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE")
