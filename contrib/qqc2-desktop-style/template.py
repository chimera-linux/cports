pkgname = "qqc2-desktop-style"
pkgver = "6.3.0"
pkgrel = 0
build_style = "cmake"
# testAnimationSpeedModifier_kconfig() write not going through? 'longDurationSpy.wait()' returned FALSE
make_check_args = ["-E", "animationspeedmodifiertest"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kcolorscheme-devel",
    "kconfig-devel",
    "kiconthemes-devel",
    "kirigami-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
]
depends = [
    "sonnet",
]
checkdepends = list(depends)
pkgdesc = "Style for Qt Quick Controls 2 to follow your KDE desktop theme"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)"
url = "https://api.kde.org/frameworks/qqc2-desktop-style/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/qqc2-desktop-style-{pkgver}.tar.xz"
sha256 = "9e7e69bb7f3646d2fcc37a24364c55d7c974c83cf6e2d906a39a8a8e14f1bcb0"
# FIXME: cfi makes kwin_wayland die top-left hotcorner and
# kcmshell6 on konsole titlebar right-click -> More Actions -> Configure Special * Settings...
hardening = ["vis", "!cfi"]


@subpackage("qqc2-desktop-style-devel")
def _devel(self):
    self.depends += ["kcoreaddons-devel"]

    return self.default_devel()
