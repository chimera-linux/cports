pkgname = "kunifiedpush"
pkgver = "25.12.1"
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
    "solid-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE library for push notifications"
license = "LGPL-2.0-or-later"
url = "https://api.kde.org/kunifiedpush/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kunifiedpush-{pkgver}.tar.xz"
)
sha256 = "68de794e3c120746a3697544f79039a8352302f7944513c991b8e32063656087"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kunifiedpush-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
