pkgname = "kpipewire"
pkgver = "6.1.3"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pipewire",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "kcoreaddons-devel",
    "ki18n-devel",
    "libva-devel",
    "pipewire-devel",
    "plasma-wayland-protocols",
    "qt6-qtdeclarative-devel",
    "qt6-qtwayland-devel",
]
pkgdesc = "KDE Components for Flatpak pipewire usage in Plasma"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kpipewire"
source = f"$(KDE_SITE)/plasma/{pkgver}/kpipewire-{pkgver}.tar.xz"
sha256 = "eb2217024e3bf3a4777548b9a0bda88ca0b97912d20336b03f5942b28b1baef9"
# CFI: breaks at least mediamonitortest (further) and xwaylandvideobridge upon screen share
hardening = ["vis", "!cfi"]
# only available test needs running pipewire
options = ["!check"]


@subpackage("kpipewire-devel")
def _devel(self):
    self.depends += ["pipewire-devel"]

    return self.default_devel()
