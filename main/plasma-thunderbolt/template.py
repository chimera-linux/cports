pkgname = "plasma-thunderbolt"
pkgver = "6.4.3"
pkgrel = 0
build_style = "cmake"
# fail to register on fakeserver for some reason
make_check_args = ["-E", "(libkbolt-managertest|kbolt-kded-kdedtest)"]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
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
    "kdbusaddons-devel",
    "ki18n-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
]
depends = ["bolt"]
checkdepends = [
    "dbus",
    "xwayland-run",
    *depends,
]
pkgdesc = "KDE integration for controlling Thunderbolt devices"
license = "GPL-2.0-only OR GPL-3.0-only"
url = "https://invent.kde.org/plasma/plasma-thunderbolt"
source = f"$(KDE_SITE)/plasma/{pkgver}/plasma-thunderbolt-{pkgver}.tar.xz"
sha256 = "6989f9d61aa8b4fa21da23de00b23164ed15375986d27160191a90b5ac133f52"
