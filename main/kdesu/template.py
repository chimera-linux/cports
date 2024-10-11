pkgname = "kdesu"
pkgver = "6.7.0"
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
sha256 = "41091ea45c6e22e1411d89d1538b2c8bd98bdc1f38d59df3e9c423aac0224e28"
hardening = ["vis"]


@subpackage("kdesu-devel")
def _(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()
