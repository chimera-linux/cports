pkgname = "kcolorscheme"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
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
pkgdesc = "KDE library to interact with KColorScheme"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-or-later"
url = "https://invent.kde.org/frameworks/kcolorscheme"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kcolorscheme-{pkgver}.tar.xz"
sha256 = "311730bdcf81009f5a79694f135a93040a4a83a66cb942d9617fcd6976049035"
hardening = ["vis", "!cfi"]


@subpackage("kcolorscheme-devel")
def _devel(self):
    self.depends += ["kconfig-devel"]

    return self.default_devel()
