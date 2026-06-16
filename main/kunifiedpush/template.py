pkgname = "kunifiedpush"
pkgver = "26.04.2"
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
url = "https://api.kde.org/kunifiedpush/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kunifiedpush-{pkgver}.tar.xz"
)
sha256 = "15b6c7c463953b0d3b0ae8dfdde9dea41ae7eac77d036ca95db6f87d1a8a8fe1"


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kunifiedpush-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
