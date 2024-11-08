pkgname = "lxqt-panel"
pkgver = "2.1.1"
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
    "libsensors-devel",
    "libstatgrab-devel",
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "LXQt desktop panel"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-panel"
source = f"{url}/releases/download/{pkgver}/lxqt-panel-{pkgver}.tar.xz"
sha256 = "176d1638f2bc0669afc0f3ff34da3faa543f2e2dac5122fd0ec235eea98986d5"
