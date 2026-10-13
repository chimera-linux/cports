pkgname = "krunner"
pkgver = "6.31.0"
pkgrel = 0
build_style = "cmake"
# FIXME: similar tests broken on alpine, everything can work in the right env
# threading is flaky
make_check_args = [
    "-E",
    "(dbusrunner|threading|runnermanager(singlerunnermode|))test",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "kwindowsystem-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Framework for providing different actions given a string query"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://community.kde.org/Frameworks"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/krunner-{pkgver}.tar.xz"
sha256 = "9bcc2525842991bf0e13d8fe7d98986c8ee770e722eda8c9e1abd609f1d65492"
hardening = ["vis"]


@subpackage("krunner-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
