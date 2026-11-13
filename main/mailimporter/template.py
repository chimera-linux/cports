pkgname = "mailimporter"
pkgver = "26.08.3"
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
    "akonadi-devel",
    "akonadi-mime-devel",
    "karchive-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kmime-devel",
    "pimcommon-devel",
    "qt6-qtdeclarative-devel",
]
checkdepends = ["xwayland-run"]
pkgdesc = "KDE PIM library for importing mail"
license = "LGPL-2.0-or-later AND GPL-2.0-only"
url = "https://community.kde.org/KDE_PIM"
source = (
    f"$(KDE_SITE)/release-service/{pkgver}/src/mailimporter-{pkgver}.tar.xz"
)
sha256 = "fd9dfee4e15a922f284575a68bdfb2e45613f207bdaeda07907d7562936d7f32"


@subpackage("mailimporter-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
