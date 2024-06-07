pkgname = "kconfig"
pkgver = "6.3.0"
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
sha256 = "8d809aaf7b5151ecd797c601c7f2701bc426b66d431b52069c7ff3b4002d7979"
# FIXME: cfi breaks at least 5 tests
hardening = ["vis", "!cfi"]


@subpackage("kconfig-devel")
def _devel(self):
    self.depends += ["qt6-qtdeclarative-devel"]

    return self.default_devel()
