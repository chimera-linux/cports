pkgname = "kunifiedpush"
pkgver = "26.08.1"
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
    "kcrash-devel",
    "ki18n-devel",
    "kservice-devel",
    "qt6-qtbase-devel",
    "qt6-qtwebsockets-devel",
    "solid-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE library for push notifications"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/libraries/kunifiedpush"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kunifiedpush-{pkgver}.tar.xz"
)
sha256 = "818476fbf87df903f92f875302ab9d76fc136d05f42530d35f58f3cc10f0a904"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kunifiedpush-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
