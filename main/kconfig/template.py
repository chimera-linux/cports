pkgname = "kconfig"
pkgver = "6.6.0"
pkgrel = 0
build_style = "cmake"
# FIXME: kconfigtest can work with right env
make_check_args = ["-E", "kconfigcore-(kconfigtest|test_kconf_update)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
]
makedepends = [
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = [
    "bash",
    "dbus",
]
pkgdesc = "KDE Persistent platform-independent application settings"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kconfig/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kconfig-{pkgver}.tar.xz"
sha256 = "070bd019b07e15201e4c7072b71337c75f6917407406a1a7107fca1bff2855fe"
hardening = ["vis"]


@subpackage("kconfig-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
