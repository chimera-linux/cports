pkgname = "kcolorscheme"
pkgver = "6.7.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE library to interact with KColorScheme"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kcolorscheme"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcolorscheme-{pkgver}.tar.xz"
sha256 = "1b4c6e84f1dd96b2ee62be755f60da60d61ba80d6709eeb3186d8882e72e2130"
hardening = ["vis"]


@subpackage("kcolorscheme-devel")
def _(self):
    self.depends += ["kconfig-devel"]

    return self.default_devel()
