pkgname = "kdeconnect"
pkgver = "25.08.0"
pkgrel = 0
build_style = "cmake"
# needs more setup
make_check_args = ["-E", "mdnstest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
    "kitemmodels-devel",
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
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtconnectivity-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtwayland-devel",
    "solid-devel",
    "wayland-protocols",
]
depends = [
    "kirigami-addons",
    "sshfs",
]
checkdepends = [*depends]
pkgdesc = "KDE plugin for communicating with a smartphone device"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://community.kde.org/KDEConnect"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdeconnect-kde-{pkgver}.tar.xz"
)
sha256 = "edc6d8d5bb3aab53208a229528ef36a5bc959bfaec17512b5621502d1d37d260"


def post_install(self):
    # stray single static lib and nothing else (?)
    self.uninstall("usr/lib/libkdeconnectinterfaces.a")
    # wrong name
    self.rename("usr/share/zsh/site-functions/_kdeconnect", "_kdeconnect-cli")
