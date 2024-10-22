pkgname = "xdg-desktop-portal-kde"
pkgver = "6.2.2"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-devel",
    "knotifications-devel",
    "kstatusnotifieritem-devel",
    "kwayland-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
    "wayland-protocols",
]
depends = [
    "kiconthemes",
    "kio-fuse",
    "plasma-workspace",
    "xdg-desktop-portal",
]
checkdepends = [
    "dbus",
    "python-gobject",
    *depends,
]
pkgdesc = "Backend implementation for xdg-desktop-portal using Qt/KF6"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/plasma/xdg-desktop-portal-kde"
source = f"$(KDE_SITE)/plasma/{pkgver}/xdg-desktop-portal-kde-{pkgver}.tar.xz"
sha256 = "669f9c1446a9b73490c3ed142895b22738eda9887eecbf62ccd9d6d1050a3dd3"
hardening = ["vis"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")
