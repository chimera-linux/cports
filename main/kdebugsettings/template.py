pkgname = "kdebugsettings"
pkgver = "26.08.0"
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
sha256 = "954f2dbb1135431e7aa75939282e705204b486ac69912f1ea8fc0f20c5024d47"
