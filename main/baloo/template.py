pkgname = "baloo"
pkgver = "6.27.0"
pkgrel = 0
build_style = "cmake"
# flaky tests when parallel
make_check_args = ["-j1"]
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
    "kdbusaddons-devel",
    "kfilemetadata-devel",
    "ki18n-devel",
    "kidletime-devel",
    "kio-devel",
    "lmdb-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "solid-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Framework for searching and metadata"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/frameworks/baloo/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/baloo-{pkgver}.tar.xz"
sha256 = "6b226118bde28e81217f8cd6129f6e24c5d422bd7a322fe682e592b028b72db7"
hardening = ["vis"]


def post_install(self):
    # TODO: dinit user service with graphical
    self.uninstall("usr/lib/systemd/user")


@subpackage("baloo-devel")
def _(self):
    self.depends += [
        "qt6-qtbase-devel",
        "kcoreaddons-devel",
        "kfilemetadata-devel",
        "lmdb-devel",
    ]
    return self.default_devel()
