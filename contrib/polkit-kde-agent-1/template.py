pkgname = "polkit-kde-agent-1"
pkgver = "6.1.5"
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
    "polkit-qt-1-devel",
    "ki18n-devel",
    "kcrash-devel",
    "kwindowsystem-devel",
    "kdbusaddons-devel",
    "kcoreaddons-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE polkit authentication daemon"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://invent.kde.org/plasma/polkit-kde-agent-1"
source = f"$(KDE_SITE)/plasma/{pkgver}/polkit-kde-agent-1-{pkgver}.tar.xz"
sha256 = "0965e5ffad432a3e6ee9e35540efcb7b4083200a48c69d91e525c09a47b920f6"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")
