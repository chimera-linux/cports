pkgname = "kdebugsettings"
pkgver = "24.12.0"
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
    "kcoreaddons-devel",
    "kconfig-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kwidgetsaddons-devel",
    "kcompletion-devel",
    "kxmlgui-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE QLoggingCategory display editor"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kdebugsettings"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdebugsettings-{pkgver}.tar.xz"
)
sha256 = "3aaef428148e92882eb184967ba73d92e053d35cb86a0157e91609089a97aaf9"
