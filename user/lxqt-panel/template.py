pkgname = "lxqt-panel"
pkgver = "2.4.1"
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
sha256 = "7828d7e8fabf66ef1491e50b609b8eb041d74c433554f7d073ac07af26843d02"
options = ["etcfiles"]
