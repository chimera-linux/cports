pkgname = "polkit-kde-agent-1"
pkgver = "6.6.5"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "knotifications-devel",
    "kwindowsystem-devel",
    "polkit-qt-1-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE polkit authentication daemon"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/polkit-kde-agent-1"
source = f"$(KDE_SITE)/plasma/{pkgver}/polkit-kde-agent-1-{pkgver}.tar.xz"
sha256 = "91990b9cd13f205a9963f88fe605942b9e8b6ee9e9103431216bf511944ce127"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical (
    # also "Passed session and the session the caller is in differs. They must be equal for now."
    self.uninstall("usr/lib/systemd/user")
