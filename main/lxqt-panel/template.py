pkgname = "lxqt-panel"
pkgver = "2.2.0"
pkgrel = 0
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
sha256 = "e5011840140fe1c06cfe4deadbb1a88c0395b33d274c2a68d7e657b6622f1adb"
