pkgname = "polkit-kde-agent-1"
pkgver = "6.4.4"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "2c218f4e66f5f933b9cdd0c6886f53625a2bf7f1c8df64bb485835ae72877e3d"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical (
    # also "Passed session and the session the caller is in differs. They must be equal for now."
    self.uninstall("usr/lib/systemd/user")
