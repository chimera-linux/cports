pkgname = "akonadi-mime"
pkgver = "26.04.2"
pkgrel = 0
build_style = "cmake"
# broken for some reason
make_check_args = ["-E", "mailserializerplugintest"]
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "libxslt-progs",
    "ninja",
    "pkgconf",
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
license = "LGPL-3.0-only"
url = "https://api.kde.org/kdepim/akonadi-mime/html"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/akonadi-mime-{pkgver}.tar.xz"
)
sha256 = "fcad2a4b4ab3f2deec9f8f0694d11e9620092b33e0923a47bf434569a89bac14"


@subpackage("akonadi-mime-devel")
def _(self):
    self.depends += ["akonadi-devel"]
    return self.default_devel()
