pkgname = "libkdegames"
pkgver = "25.08.0"
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
sha256 = "15579343d5b06608115e8e95473b80bc91de8841b1a79584f5615a91fe57e2f7"


@subpackage("libkdegames-devel")
def _(self):
    return self.default_devel()


@subpackage("libkdegames-carddecks")
def _(self):
    self.subdesc = "card decks for KDE card games"
    return ["usr/share/carddecks"]
