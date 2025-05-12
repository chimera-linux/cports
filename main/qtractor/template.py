pkgname = "qtractor"
pkgver = "1.5.4"
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
license = "GPL-2.0-or-later"
url = "https://www.qtractor.org"
source = f"$(SOURCEFORGE_SITE)/qtractor/qtractor-{pkgver}.tar.gz"
sha256 = "815e8880503b19e9de69b44293a1cb65531f9d2f78a9b760c89406c3044ef74e"
