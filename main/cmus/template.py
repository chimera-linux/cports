pkgname = "cmus"
pkgver = "2.12.0"
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
    "faad2-devel",
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
license = "GPL-2.0-or-later"
url = "https://cmus.github.io"
source = f"https://github.com/cmus/cmus/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "44b96cd5f84b0d84c33097c48454232d5e6a19cd33b9b6503ba9c13b6686bfc7"
# no tests
options = ["!check"]


def init_configure(self):
    self.configure_args += [
        "HOSTCC=" + self.get_tool("CC"),
        "LD=" + self.get_tool("CC"),
    ]
