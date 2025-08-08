pkgname = "kcolorscheme"
pkgver = "6.17.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "kconfig-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "qt6-qtbase-private-devel",  # qguiapplication_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE library to interact with KColorScheme"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kcolorscheme"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kcolorscheme-{pkgver}.tar.xz"
sha256 = "c8bd45eb248fc38d816e4eb0fd949d909c09a3a5a90848ef6d4040c35973f7b4"
hardening = ["vis"]


@subpackage("kcolorscheme-devel")
def _(self):
    self.depends += ["kconfig-devel"]

    return self.default_devel()
