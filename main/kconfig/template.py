pkgname = "kconfig"
pkgver = "6.9.0"
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
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kconfig-{pkgver}.tar.xz"
sha256 = "b8b9dfb0bc5bc0f9c45164e02c988dd8ab10a34aea0c80b1945fd0b3267ac6f9"
hardening = ["vis"]


@subpackage("kconfig-devel")
def _(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
