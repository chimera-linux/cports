pkgname = "kunifiedpush"
pkgver = "26.08.0"
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
sha256 = "abd4a67798428023913a5343de747ec40fc7b2a19ed4a4f18650df9c755abd80"
options = ["etcfiles"]


def post_install(self):
    self.uninstall("usr/lib/systemd/user")


@subpackage("kunifiedpush-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
