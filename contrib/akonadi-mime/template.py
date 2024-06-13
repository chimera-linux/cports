pkgname = "akonadi-mime"
pkgver = "24.05.1"
pkgrel = 0
build_style = "cmake"
# broken for some reason
make_check_args = ["-E", "mailserializerplugintest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "akonadi-devel",
    "ki18n-devel",
    "kio-devel",
    "kitemmodels-devel",
    "kmime-devel",
    "kxmlgui-devel",
    "libxslt-devel",
    "qt6-qtdeclarative-devel",
    "shared-mime-info",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE Akonadi mime libraries"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/akonadi-mime/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-mime-{pkgver}.tar.xz"
)
sha256 = "524280cac966f9a4490af14c5186e6e107905be9f05be33430f525e8f0a60600"


@subpackage("akonadi-mime-devel")
def _devel(self):
    self.depends += ["akonadi-devel"]
    return self.default_devel()
