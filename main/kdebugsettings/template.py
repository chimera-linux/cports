pkgname = "kdebugsettings"
pkgver = "26.08.1"
pkgrel = 0
build_style = "cmake"
# dies quietly
make_check_args = ["-E", "kdebugsettings-self-test"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtbase-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE QLoggingCategory display editor"
license = "LGPL-2.1-or-later"
url = "https://apps.kde.org/kdebugsettings"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kdebugsettings-{pkgver}.tar.xz"
)
sha256 = "9e0a64d0eacc69b4b61c3e8d27d2e34c7c478e1a7c4b111f9e3fcb83018af2a0"
