pkgname = "obs-studio"
pkgver = "31.0.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_COMPILE_WARNING_AS_ERROR=OFF",
    "-DCMAKE_POSITION_INDEPENDENT_CODE=ON",
    "-DOBS_CMAKE_VERSION=3.0.0",
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
    "curl-devel",
    "ffmpeg-devel",
    "fontconfig-devel",
    "freetype-devel",
    "jansson-devel",
    "libdatachannel-devel",
    "libpulse-devel",
    "librist-devel",
    "libva-devel",
    "libx11-devel",
    "libxcb-devel",
    "libxkbcommon-devel",
    "mbedtls-devel-static",
    "mesa-devel",
    "nlohmann-json",
    "nv-codec-headers",
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
license = "GPL-2.0-or-later"
url = "https://obsproject.com"
source = f"https://github.com/obsproject/obs-studio/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f0b53f0acd05ac0dc3044bd3700740f9d2b7a13504d55c0107468e84a860742b"
hardening = ["vis", "!cfi"]
# don't build with lto
options = ["!check"]


@subpackage("obs-studio-devel")
def _(self):
    return self.default_devel()
