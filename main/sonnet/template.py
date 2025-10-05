pkgname = "sonnet"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "aspell",
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "aspell-devel",
    "hunspell-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    # TODO: hspell/voikko?
]
# depends = ["hunspell", "aspell-en"]
pkgdesc = "KDE Multi-language spell checker"
license = "LGPL-2.1-only"
url = "https://develop.kde.org/docs/features/spellchecking"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/sonnet-{pkgver}.tar.xz"
sha256 = "2d94c957a3c5f2232653ad782b291e2b959eea6dca83cc09cae621bc9834ab25"
hardening = ["vis"]


@subpackage("sonnet-devel")
def _(self):
    return self.default_devel()
