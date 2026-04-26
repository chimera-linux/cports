pkgname = "chipass"
pkgver = "2026.09.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCHIPASS_WITH_UPDATE_CHECK=OFF"]
# TODO fix the focus issues without heavy compositor and serial execution
# https://codeberg.org/ChiPass/ChiPass/issues/193
make_check_args = ["-j1"]
make_check_wrapper = ["wlheadless-run", "-c", "kwin", "--"]
hostmakedepends = [
    "appstream",
    "asciidoctor",
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "argon2-devel",
    "botan-devel",
    "libusb-devel",
    "libx11-devel",
    "libxtst-devel",
    "minizip-devel",
    "pcsc-lite-devel",
    "qrencode-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "qt6-qttranslations",
    "zlib-ng-compat-devel",
]
depends = [
    # TODO maybe make them optional?
    "cmd:wl-copy!wl-clipboard",
    "cmd:xclip!xclip",
]
checkdepends = ["kwin", "xwayland-run"]
pkgdesc = "Password manager"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://codeberg.org/ChiPass/ChiPass"
source = f"https://codeberg.org/ChiPass/ChiPass/releases/download/v{pkgver}/ChiPass-{pkgver}-source.tar.bz2"
sha256 = "0e0fa8d3ccd3652c04bb82226fc85a6af505b60325a8f09ab94fcb4a6013f8a8"
hardening = ["vis", "cfi"]
