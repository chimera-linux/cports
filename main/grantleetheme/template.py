pkgname = "grantleetheme"
pkgver = "25.04.1"
pkgrel = 0
build_style = "cmake"
# can't find itself
make_check_args = ["-E", "grantleethemetest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "knewstuff-devel",
    "ktexttemplate-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Grantlee template theme library"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/pim/grantleetheme"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantleetheme-{pkgver}.tar.xz"
)
sha256 = "fa60b7cc5cb47e8575fcb8f091d2ead33d751159d4d2118e65dc713a1acb7d5c"


@subpackage("grantleetheme-devel")
def _(self):
    self.depends += ["ktexttemplate-devel"]
    return self.default_devel()
