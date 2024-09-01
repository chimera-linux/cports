pkgname = "sonnet"
pkgver = "6.5.0"
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
sha256 = "7e86b6f82b7951c3e81cea75f79baf7a8a0f884fcb024f02a6153a467a3de1aa"
hardening = ["vis"]


@subpackage("sonnet-devel")
def _(self):
    return self.default_devel()
