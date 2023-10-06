pkgname = "obs-studio"
pkgver = "29.1.3"
pkgrel = 1
build_style = "cmake"
configure_args = [
    f"-DOBS_VERSION_OVERRIDE={pkgver}",
    "-DENABLE_ALSA=OFF",
    "-DENABLE_AJA=OFF",
    "-DENABLE_JACK=ON",
    # XXX: python+lua scripting is checked at once, latter needs luajit
    "-DENABLE_SCRIPTING=OFF",
    "-DENABLE_VLC=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python",
    "qt6-qtbase",
    "swig",
]
makedepends = [
    "ffmpeg-devel",
    "fontconfig-devel",
    "freetype-devel",
    "jansson-devel",
    "libcurl-devel",
    "libpulse-devel",
    "librist-devel",
    "libva-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mbedtls-devel",
    "mesa-devel",
    "pciutils-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "python-devel",
    "qt6-qtbase-devel",
    "qt6-qtsvg-devel",
    "speexdsp-devel",
    "srt-devel",
    "udev-devel",
    "v4l-utils-devel",
    "wayland-devel",
    "x264-devel",
]
pkgdesc = (
    "Free and open source software for live streaming and screen recording"
)
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://obsproject.com"
source = f"https://github.com/obsproject/obs-studio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "9d9cfbdbdd255f48a23feeefb60089769a65f52bbca24fa31d74125f3bbb0e90"
# FIXME: cfi
hardening = ["vis"]
# don't build with lto
options = ["!check"]


@subpackage("obs-studio-devel")
def _devel(self):
    return self.default_devel()
