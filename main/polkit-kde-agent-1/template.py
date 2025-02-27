pkgname = "polkit-kde-agent-1"
pkgver = "6.3.2"
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
    "polkit-qt-1-devel",
    "ki18n-devel",
    "kcrash-devel",
    "kwindowsystem-devel",
    "kdbusaddons-devel",
    "kcoreaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE polkit authentication daemon"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/polkit-kde-agent-1"
source = f"$(KDE_SITE)/plasma/{pkgver}/polkit-kde-agent-1-{pkgver}.tar.xz"
sha256 = "b9fa047ed16066f87acb8e07cd28a66a04b9a9bbe696b1995b19112cb39f9e8c"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical (
    # also "Passed session and the session the caller is in differs. They must be equal for now."
    self.uninstall("usr/lib/systemd/user")
