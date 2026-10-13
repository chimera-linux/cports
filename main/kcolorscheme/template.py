pkgname = "kcolorscheme"
pkgver = "6.31.0"
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
sha256 = "41a8b12a4d9f4fdada70e4853879a2f43a7bf43e870a18c6038eebd956a1f863"
hardening = ["vis"]


@subpackage("kcolorscheme-devel")
def _(self):
    self.depends += ["kconfig-devel"]

    return self.default_devel()
