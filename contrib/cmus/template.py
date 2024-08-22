pkgname = "cmus"
pkgver = "2.11.0"
pkgrel = 2
build_style = "configure"
configure_args = [
    "prefix=/usr",
    "CONFIG_ALSA=n",
    "CONFIG_OSS=n",
    "CONFIG_MPRIS=y",
    "CONFIG_FFMPEG=y",
    "CONFIG_FLAC=y",
    "CONFIG_CDDB=y",
    "CONFIG_CDIO=y",
    "CONFIG_MODPLUG=y",
    "CONFIG_PULSE=y",
    "CONFIG_SAMPLERATE=y",
    "CONFIG_VORBIS=y",
    "CONFIG_OPUS=y",
    "CONFIG_JACK=y",
    "CONFIG_WAVPACK=y",
]
hostmakedepends = ["pkgconf", "bash"]
makedepends = [
    "elogind-devel",
    "ffmpeg-devel",
    "flac-devel",
    "libcddb-devel",
    "libcdio-paranoia-devel",
    "libmodplug-devel",
    "libpulse-devel",
    "libsamplerate-devel",
    "libvorbis-devel",
    "linux-headers",
    "ncurses-devel",
    "opusfile-devel",
    "pipewire-jack-devel",
    "wavpack-devel",
]
pkgdesc = "Console music player"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://cmus.github.io"
source = f"https://github.com/cmus/cmus/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2bbdcd6bbbae301d734214eab791e3755baf4d16db24a44626961a489aa5e0f7"
# no tests
options = ["!check"]


def init_configure(self):
    self.configure_args += [
        "HOSTCC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
    ]
