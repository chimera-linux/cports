pkgname = "flameshot"
pkgver = "14.0.0"
pkgrel = 0
_qt_color_widgets_rev = "3.0.0"
build_style = "cmake"
configure_args = ["-DUSE_BUNDLED_KDSINGLEAPPLICATION=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "kdsingleapplication-devel",
    "kguiaddons-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
]
pkgdesc = "Powerful screenshot software"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://flameshot.org"
source = [
    f"https://github.com/flameshot-org/flameshot/archive/refs/tags/v{pkgver}.tar.gz",
    f"https://gitlab.com/mattbas/Qt-Color-Widgets/-/archive/{_qt_color_widgets_rev}/Qt-Color-Widgets-{_qt_color_widgets_rev}.tar.gz",
]
source_paths = [".", "external/Qt-Color-Widgets"]
sha256 = [
    "810c399f3b9fbfd72e24e61417ede24243925f9c0d03040a8aba0d4866676d93",
    "8b8020d661894ece5bfb96d0b4e2e0e15db69839a986b59f8748f12c603e021b",
]
