pkgname = "sonnet"
pkgver = "6.28.0"
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
sha256 = "66c6b439950bec7f67b730e6e49d6d30cba21dad115e4a47c4fe46014cc19c3b"
hardening = ["vis"]


@subpackage("sonnet-devel")
def _(self):
    return self.default_devel()
