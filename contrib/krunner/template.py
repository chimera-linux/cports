pkgname = "krunner"
pkgver = "6.2.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/krunner/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/krunner-{pkgver}.tar.xz"
sha256 = "f18f1578ff8c76c455837a4bc9a3e71273bba4ac54afd24e143a9dc20706041f"
# FIXME: cfi breaks at least a bunch of tests
hardening = ["vis", "!cfi"]


@subpackage("krunner-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
