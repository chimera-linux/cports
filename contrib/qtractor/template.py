pkgname = "qtractor"
pkgver = "0.9.91"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCONFIG_WAYLAND=1"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "aubio-devel",
    "ladspa-sdk",
    "liblo-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "lilv-devel",
    "pipewire-jack-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "qt6-qttools-devel",
    "rubberband-devel",
]
pkgdesc = "Audio/MIDI multi-track sequencer"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://www.qtractor.org"
source = f"$(SOURCEFORGE_SITE)/qtractor/qtractor-{pkgver}.tar.gz"
sha256 = "865afcc04fcaee1b8f14875fe3e0b989444f1464221ab44f14a2f23885e485ce"
