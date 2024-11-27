pkgname = "deadbeef"
pkgver = "1.9.6"
pkgrel = 1
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
    "faad2-devel",
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later AND Zlib AND BSD-2-Clause"
url = "https://deadbeef.sourceforge.io"
source = f"https://downloads.sourceforge.net/sourceforge/deadbeef/deadbeef-{pkgver}.tar.bz2"
sha256 = "9d77b3d8afdeab5027d24bd18e9cfc04ce7d6ab3ddc043cc8e84c82b41b79c04"
# plugins broken
hardening = ["!vis"]

if self.profile().endian == "big":
    broken = "libmms mod broken"


def post_install(self):
    self.install_license("COPYING")


@subpackage("deadbeef-devel")
def _(self):
    return self.default_devel()
