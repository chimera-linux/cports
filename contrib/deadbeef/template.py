pkgname = "deadbeef"
pkgver = "1.9.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # yasm
    "--disable-ffap",
    # forces -msse3 lol
    "--disable-libretro",
    # gtk2
    "--disable-gtkui",
    # prefer pipewire
    "--disable-alsa",
    "--disable-oss",
    "--disable-pulse",
    "--disable-static",
]
# broken
configure_gen = []
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "gettext",
    "gmake",
    "gtk+3-devel",
    "intltool",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "ffmpeg-devel",
    "flac-devel",
    "gtk+3-devel",
    "jansson-devel",
    "libcurl-devel",
    "libdispatch-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "libvorbis-devel",
    "libzip-devel",
    "mpg123-devel",
    "musl-bsd-headers",
    "opusfile-devel",
    "pipewire-devel",
    "wavpack-devel",
]
pkgdesc = "Modular cross-platform audio player"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND Zlib AND BSD-2-Clause"
url = "https://deadbeef.sourceforge.io"
source = f"https://downloads.sourceforge.net/sourceforge/deadbeef/deadbeef-{pkgver}.tar.bz2"
sha256 = "74c4478edccfee8a978d4adbeeb208f049bef63982f4df19ee208aaad8a6cd26"
# plugins broken
hardening = ["!vis"]

if self.profile().endian == "big":
    broken = "libmms mod broken"


def post_install(self):
    self.install_license("COPYING")


@subpackage("deadbeef-devel")
def _devel(self):
    return self.default_devel()
