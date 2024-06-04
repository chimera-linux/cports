pkgname = "kpipewire"
pkgver = "6.0.5"
pkgrel = 1
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
sha256 = "4327da2435186e90653c870de73082a7e5fb61d13e06a517cb021f1d56b7d2d6"
# FIXME: cfi breaks at least mediamonitortest (further) and xwaylandvideobridge upon screen share
hardening = ["vis", "!cfi"]
# only available test needs running pipewire
options = ["!check"]


@subpackage("kpipewire-devel")
def _devel(self):
    self.depends += ["pipewire-devel"]

    return self.default_devel()
