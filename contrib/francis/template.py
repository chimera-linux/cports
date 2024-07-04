pkgname = "francis"
pkgver = "24.05.2"
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
sha256 = "3e1350cb43e64e88e26a0780c522d28b99d20afadc187893d92067e61ee9e96d"
