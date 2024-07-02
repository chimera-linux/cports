pkgname = "lxqt-panel"
pkgver = "2.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DALSA_PLUGIN=NO",
    "-DCPULOAD_PLUGIN=NO",
    "-DNETWORKMONITOR_PLUGIN=NO",
    "-DSYSSTAT_PLUGIN=NO",
    "-DVOLUME_USE_ALSA=NO",
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
    "lxqt-globalkeys-devel",
    "lxqt-menu-data",
    "qt6-qttools-devel",
    "solid-devel",
    "xcb-util-devel",
]
depends = ["lxqt-menu-data"]
pkgdesc = "LXQt desktop panel"
maintainer = "Isaac Freund <mail@isaacfreund.com>"
license = "LGPL-2.1-or-later"
url = "https://github.com/lxqt/lxqt-panel"
source = f"{url}/releases/download/{pkgver}/lxqt-panel-{pkgver}.tar.xz"
sha256 = "73483c36e411496f8e958b7e56ba8bb06ae0b4300a62cf4c4a78964da6a59407"
