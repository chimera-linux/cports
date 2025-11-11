pkgname = "obs-studio"
pkgver = "32.0.2"
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
    "extra-cmake-modules",
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
    "libdrm-devel",
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
    "qt6-qtbase-private-devel",
    "qt6-qtsvg-devel",
    "rnnoise-devel",
    "simde",
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
sha256 = "39e99b9fbdc77e7e87cfd9c7e8709d1d427627bad5b21b791019c887c8598d13"
hardening = ["vis", "!cfi"]
# don't build with lto
options = ["!check"]


@subpackage("obs-studio-devel")
def _(self):
    return self.default_devel()
