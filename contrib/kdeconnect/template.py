pkgname = "kdeconnect"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
# needs more setup
make_check_args = ["-E", "mdnstest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "kcmutils-devel",
    "kconfigwidgets-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kpackage-devel",
    "kpeople-devel",
    "kservice-devel",
    "kstatusnotifieritem-devel",
    "kwindowsystem-devel",
    "libfakekey-devel",
    "modemmanager-qt-devel",
    "pulseaudio-qt-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtconnectivity-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "wayland-protocols",
]
depends = [
    "kirigami-addons",
    "sshfs",
]
checkdepends = ["xwayland-run", *depends]
pkgdesc = "KDE plugin for communicating with a smartphone device"
maintainer = "psykose <alice@ayaya.dev>"
license = " GPL-2.0-only OR GPL-3.0-only"
url = "https://community.kde.org/KDEConnect"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdeconnect-kde-{pkgver}.tar.xz"
)
sha256 = "cbd102cf3083d2c043e875cc4ef1ac3a33837484f440b2e7377bc9c0bd3212ae"


def post_install(self):
    # stray single static lib and nothing else (?)
    self.uninstall("usr/lib/libkdeconnectinterfaces.a")
