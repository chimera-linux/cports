pkgname = "libkdegames"
pkgver = "24.05.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.0-only"
url = "https://invent.kde.org/games/libkdegames"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/libkdegames-{pkgver}.tar.xz"
sha256 = "eaf216b7933332a0d3e0553fd759882fed22d59b3980676e5f6e976515a410eb"


@subpackage("libkdegames-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libkdegames-carddecks")
def _carddecks(self):
    self.pkgdesc = f"{pkgdesc} (card decks for KDE card games)"
    return ["usr/share/carddecks"]
