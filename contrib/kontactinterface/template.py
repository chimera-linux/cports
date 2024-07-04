pkgname = "kontactinterface"
pkgver = "24.05.2"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcoreaddons-devel",
    "ki18n-devel",
    "kparts-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "KDE Kontact plugin interface library"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/kontactinterface/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/kontactinterface-{pkgver}.tar.xz"
)
sha256 = "6c854ae5cbc937f49bc6389ad2e783bce0ab63db0af67acd28bfc49b04afe915"


@subpackage("kontactinterface-devel")
def _devel(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
