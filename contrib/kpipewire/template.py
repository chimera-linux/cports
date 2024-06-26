pkgname = "kpipewire"
pkgver = "6.1.1"
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
sha256 = "6a1d5aba6eaf530605bb22514cbb17a144d3e8c7c1a5ddf0d3a9ce6b481f7686"
# FIXME: cfi breaks at least mediamonitortest (further) and xwaylandvideobridge upon screen share
hardening = ["vis", "!cfi"]
# only available test needs running pipewire
options = ["!check"]


@subpackage("kpipewire-devel")
def _devel(self):
    self.depends += ["pipewire-devel"]

    return self.default_devel()
