pkgname = "cmus"
pkgver = "2.10.0"
pkgrel = 0
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
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "bash"]
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
sha256 = "ff40068574810a7de3990f4f69c9c47ef49e37bd31d298d372e8bcdafb973fff"
# no tests
options = ["!check"]


def init_configure(self):
    self.configure_args += [
        "HOSTCC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
    ]
