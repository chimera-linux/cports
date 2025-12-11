pkgname = "francis"
pkgver = "25.12.0"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
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
    "kdbusaddons-devel",
    "ki18n-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE pomodoro time tracker"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/francis"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/francis-{pkgver}.tar.xz"
sha256 = "8e02c4bdf5c4a2e6eec4cf23d20030f9ad4dae0cfde9fad53a5227ac376ef8eb"
