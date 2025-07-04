pkgname = "kpimtextedit"
pkgver = "25.04.3"
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
license = "LGPL-2.1-or-later"
url = "https://api.kde.org/kdepim/kpimtextedit/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kpimtextedit-{pkgver}.tar.xz"
)
sha256 = "4a107ca02a4535fdc08f7b65886cc99cdf9da642a67363bcbab4cba338bc6c32"


@subpackage("kpimtextedit-devel")
def _(self):
    return self.default_devel()
