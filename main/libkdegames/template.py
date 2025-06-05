pkgname = "libkdegames"
pkgver = "25.04.2"
pkgrel = 0
build_style = "cmake"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "karchive-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kdnssd-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knewstuff-devel",
    "kxmlgui-devel",
    "libsndfile-devel",
    "openal-soft-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtsvg-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE common games library"
license = "LGPL-2.0-only"
url = "https://invent.kde.org/games/libkdegames"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdegames-{pkgver}.tar.xz"
sha256 = "8775c78f76d64be05bab10df4d0c3fa3d5f5442a094c86501d6ec7ada9b30d2b"


@subpackage("libkdegames-devel")
def _(self):
    return self.default_devel()


@subpackage("libkdegames-carddecks")
def _(self):
    self.subdesc = "card decks for KDE card games"
    return ["usr/share/carddecks"]
