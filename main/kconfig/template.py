pkgname = "kconfig"
pkgver = "6.12.0"
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
license = "LGPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later"
url = "https://api.kde.org/frameworks/kconfig/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kconfig-{pkgver}.tar.xz"
sha256 = "03d1d09054d646c67fcaa9f1fa53157811ad07ef40a38b9f4e0b52ae3173b1bf"
hardening = ["vis"]


@subpackage("kconfig-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
