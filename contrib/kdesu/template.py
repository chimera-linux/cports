pkgname = "kdesu"
pkgver = "6.4.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "kconfig-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "kpty-devel",
    "qt6-qttools-devel",
]
pkgdesc = "KDE Framework for running commands as root"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-only"
url = "https://api.kde.org/frameworks/kdesu/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/kdesu-{pkgver}.tar.xz"
)
sha256 = "f27ae587eb5f93bb1890b414ee3eb63b25404f96f6dbd0048426b60e0acacb5a"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _devel(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()
