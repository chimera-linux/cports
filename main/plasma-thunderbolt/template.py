pkgname = "plasma-thunderbolt"
pkgver = "6.6.5"
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
sha256 = "56e3a2833096279c3a9ec1dbb4b53a5fa4bc36b3569e3f7ec191f002f40bf71f"
