pkgname = "francis"
pkgver = "24.12.1"
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
    "kirigami-devel",
    "kirigami-addons-devel",
    "knotifications-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE pomodoro time tracker"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-3.0-or-later"
url = "https://apps.kde.org/francis"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/francis-{pkgver}.tar.xz"
sha256 = "a29960ea1fad78a5b67ae21d36d2e7717599378bb8c223d7e45a8a508a73337e"
