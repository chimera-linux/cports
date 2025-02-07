pkgname = "grantleetheme"
pkgver = "24.12.2"
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/pim/grantleetheme"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/grantleetheme-{pkgver}.tar.xz"
)
sha256 = "595c2330f8ca23cf000e13a7ae6ae7c7ce2a5ed410ceefd506d017eea1dcd563"


@subpackage("grantleetheme-devel")
def _(self):
    self.depends += ["ktexttemplate-devel"]
    return self.default_devel()
