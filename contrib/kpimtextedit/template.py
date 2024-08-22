pkgname = "kpimtextedit"
pkgver = "24.08.0"
pkgrel = 0
build_style = "cmake"
# hangs
make_check_args = ["-E", "richtextcomposertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcodecs-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "ktextaddons-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
pkgdesc = "KDE PIM textedit class"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/kpimtextedit/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpimtextedit-{pkgver}.tar.xz"
)
sha256 = "abc7d5170967b010fa6ace2ff762671b5212a9de4542f3da3fc31dbe7235c0a3"


@subpackage("kpimtextedit-devel")
def _(self):
    return self.default_devel()
