pkgname = "obs-studio"
pkgver = "30.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    f"-DOBS_VERSION_OVERRIDE={pkgver}",
    "-DENABLE_ALSA=OFF",
    "-DENABLE_AJA=OFF",
    "-DENABLE_WEBRTC=ON",
    "-DENABLE_JACK=ON",
    "-DENABLE_SCRIPTING=ON",
    "-DENABLE_SCRIPTING_LUA=OFF",
    "-DENABLE_SCRIPTING_PYTHON=ON",
    "-DENABLE_VLC=OFF",
    # TODO: onevpl
    "-DENABLE_QSV11=OFF",
    "-DOPENGL_opengl_LIBRARY=/usr/lib/libGL.so",
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
    "libdatachannel-devel",
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
    "rnnoise-devel",
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
sha256 = "490bae1c392b3b344b0270afd8cb887da4bc50bd92c0c426e96713c1ccb9701a"
# FIXME: cfi
hardening = ["vis"]
# don't build with lto
options = ["!check"]


@subpackage("obs-studio-devel")
def _devel(self):
    return self.default_devel()
