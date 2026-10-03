pkgname = "polkit-kde-agent-1"
pkgver = "6.7.91"
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
source = (
    f"$(KDE_UNSTABLE_SITE)/plasma/{pkgver}/polkit-kde-agent-1-{pkgver}.tar.xz"
)
sha256 = "6c2ecdffcec5f3d66f6e64627a039cff6b333070e7c38786f4a1a4fecf65cbe6"
hardening = ["vis"]
options = ["etcfiles"]


def post_install(self):
    # TODO: dinit user service with graphical (
    # also "Passed session and the session the caller is in differs. They must be equal for now."
    self.uninstall("usr/lib/systemd/user")
