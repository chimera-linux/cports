pkgname = "sonnet"
pkgver = "6.6.0"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-only"
url = "https://develop.kde.org/docs/features/spellchecking"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/sonnet-{pkgver}.tar.xz"
sha256 = "2f8a5ef2d5264a31af686efa8fe31372837edc5317f3103395dd389c37237316"
hardening = ["vis"]


@subpackage("sonnet-devel")
def _(self):
    return self.default_devel()
