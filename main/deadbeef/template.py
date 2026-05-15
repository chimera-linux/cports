pkgname = "deadbeef"
pkgver = "1.10.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    # yasm
    "--disable-ffap",
    # forces -msse3 lol
    "--disable-libretro",
    # prefer pipewire
    "--disable-alsa",
    "--disable-oss",
    "--disable-pulse",
    "--disable-static",
]
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gtk+3-devel",
    "intltool",
    "libtool",
    "pkgconf",
]
makedepends = [
    "alsa-lib-devel",
    "curl-devel",
    "faad2-devel",
    "flac-devel",
    "gtk+3-devel",
    "jansson-devel",
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
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND Zlib AND BSD-2-Clause"
url = "https://deadbeef.sourceforge.io"
source = f"https://downloads.sourceforge.net/sourceforge/deadbeef/deadbeef-{pkgver}.tar.bz2"
sha256 = "dd951e83e0069e2f3df18985dd40d2cf9409f502b0ecaaf1ac229d5009a8e698"
# plugins broken
hardening = ["!vis"]

if self.profile().endian == "big":
    broken = "libmms mod broken"


def post_install(self):
    self.install_license("COPYING")


@subpackage("deadbeef-devel")
def _(self):
    return self.default_devel()
