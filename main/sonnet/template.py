pkgname = "sonnet"
pkgver = "6.7.0"
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
sha256 = "2f970d490effd668e64dd93ffef344a80db7e63130bb23df4fa0d6b14150e588"
hardening = ["vis"]


@subpackage("sonnet-devel")
def _(self):
    return self.default_devel()
