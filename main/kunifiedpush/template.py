pkgname = "kunifiedpush"
pkgver = "1.0.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcmutils-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kservice-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebsockets-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE library for push notifications"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kunifiedpush/html"
source = f"$(KDE_SITE)/kunifiedpush/kunifiedpush-{pkgver}.tar.xz"
sha256 = "2ddeba21306d0307114ec50a2c38159ec62359f9fc6cdd58da30a369fbd550cf"


@subpackage("kunifiedpush-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
