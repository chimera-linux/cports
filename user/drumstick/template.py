pkgname = "drumstick"
pkgver = "2.9.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = [
    "cmake",
    "doxygen",
    "graphviz",
    "ninja",
    "pkgconf",
    "shared-mime-info",
]
makedepends = [
    "alsa-lib-devel",
    "fluidsynth-devel",
    "libpulse-devel",
    "pipewire-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
    "sonivox-devel",
]
pkgdesc = "MIDI libraries for Qt"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://drumstick.sourceforge.io"
source = f"$(SOURCEFORGE_SITE)/drumstick/drumstick-{pkgver}.tar.gz"
sha256 = "a7049333d5411faf4d91a81ae666746106b578897fc0713a84325f65fdd06ffb"


@subpackage("drumstick-devel")
def _(self):
    return self.default_devel()
