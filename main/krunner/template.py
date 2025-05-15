pkgname = "krunner"
pkgver = "6.14.0"
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
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kitemmodels-devel",
    "plasma-activities-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = [
    "dbus",
]
pkgdesc = "KDE Framework for providing different actions given a string query"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/krunner/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/krunner-{pkgver}.tar.xz"
sha256 = "138cfb98cd73392722f4499408d075a2c7705bdbf436ecc077360c3153db2fa6"
hardening = ["vis"]


@subpackage("krunner-devel")
def _(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
