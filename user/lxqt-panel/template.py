pkgname = "lxqt-panel"
pkgver = "2.2.2"
pkgrel = 1
build_style = "cmake"
configure_args = [
    "-DSYSSTAT_PLUGIN=OFF",
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
sha256 = "5d150e7a4e8818715b8f4eec7f4bb26c98f740cd56f972199b35fc7c81da1969"
