pkgname = "lxqt-panel"
pkgver = "2.5.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DVOLUME_USE_ALSA=OFF",
]
hostmakedepends = [
    "cmake",
    "lxqt-build-tools",
    "ninja",
    "perl",
    "pkgconf",
]
makedepends = [
    "kwindowsystem-devel",
    "layer-shell-qt-devel",
    "libdbusmenu-lxqt-devel",
    "liblxqt-devel",
    "libpulse-devel",
    "libstatgrab-devel",
    "libsysstat-devel",
    "lm-sensors-devel",
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "qt6-qtbase-private-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "LXQt desktop panel"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-panel"
source = f"{url}/releases/download/{pkgver}/lxqt-panel-{pkgver}.tar.xz"
sha256 = "7a96abec41355d2e42d4e4d8a03cfb064647729e9e292781c126f12e2a699e7d"
options = ["etcfiles"]
