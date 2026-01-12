pkgname = "kpipewire"
pkgver = "6.5.4"
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
license = "LGPL-2.1-or-later"
url = "https://invent.kde.org/plasma/kpipewire"
source = f"$(KDE_SITE)/plasma/{pkgver}/kpipewire-{pkgver}.tar.xz"
sha256 = "fc89ef7ccdcdbbdc55b9147420f5f5cf85bf3902c07b3ae0c0dbf9d4a23ba48a"
hardening = ["vis"]
# only available test needs running pipewire
options = ["!check"]


@subpackage("kpipewire-devel")
def _(self):
    self.depends += ["pipewire-devel"]

    return self.default_devel()
