pkgname = "kdesu"
pkgver = "6.2.0"
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
sha256 = "7c612fea489d9e3e3d3c90cab0d314d98486bdc06014a60f609fdff21505822f"
# CFI: test
hardening = ["vis", "!cfi"]


@subpackage("kdesu-devel")
def _devel(self):
    self.depends += ["kpty-devel"]
    return self.default_devel()
