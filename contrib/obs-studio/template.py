pkgname = "obs-studio"
pkgver = "30.2.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    f"-DOBS_VERSION_OVERRIDE={pkgver}",
    "-DENABLE_ALSA=OFF",
    "-DENABLE_AJA=OFF",
    "-DENABLE_JACK=ON",
    # won't work without proprietary nvidia drivers
    "-DENABLE_NATIVE_NVENC=OFF",
    # TODO: onevpl
    "-DENABLE_QSV11=OFF",
    "-DENABLE_SCRIPTING=ON",
    "-DENABLE_SCRIPTING_LUA=OFF",
    "-DENABLE_SCRIPTING_PYTHON=ON",
    "-DENABLE_VLC=OFF",
    "-DENABLE_WEBRTC=ON",
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
    "nlohmann-json",
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
    "uthash",
    "v4l-utils-devel",
    "wayland-devel",
    "x264-devel",
]
pkgdesc = "Live streaming and screen recording software"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://obsproject.com"
source = f"https://github.com/obsproject/obs-studio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ce8c6ae586df17fef6c2473883531291010dfbb8fc1ce20582e23d3c41df41ba"
hardening = ["vis", "!cfi"]
# don't build with lto
options = ["!check"]


@subpackage("obs-studio-devel")
def _devel(self):
    return self.default_devel()
