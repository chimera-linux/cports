pkgname = "flameshot"
pkgver = "13.3.0"
pkgrel = 0
_qt_color_widgets_rev = "352bc8f99bf2174d5724ee70623427aa31ddc26a"
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
source_paths = [".", "qt-color-widgets"]
sha256 = [
    "bd1666313c875400e9588b47eb3fd2f4d0828460b3705a215b97746ea654c1b4",
    "fba0319194bd99649be6646f3f4c39d6b5467e3d0eceb0b8a53a48ae6b9fdcb2",
]


def post_extract(self):
    self.mkdir("external")
    self.mv("qt-color-widgets", "external/Qt-Color-Widgets")


def post_install(self):
    self.install_license("LICENSE")
