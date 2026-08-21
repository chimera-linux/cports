pkgname = "mailimporter"
pkgver = "26.08.0"
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
sha256 = "c61402add7fe11b249e565f8cbe7574f86b170e89a667de0833d40a9f4098465"


@subpackage("mailimporter-devel")
def _(self):
    self.depends += ["karchive-devel"]
    return self.default_devel()
