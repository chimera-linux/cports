pkgname = "kontactinterface"
pkgver = "24.08.2"
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
sha256 = "9aadaa1e014ba18482318eae67559ca53c15ced638c85ba64cd7e85ba6196957"


@subpackage("kontactinterface-devel")
def _(self):
    self.depends += ["kparts-devel"]
    return self.default_devel()
