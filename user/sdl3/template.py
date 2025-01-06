pkgname = "sdl3"
pkgver = "3.1.8"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DCMAKE_BUILD_TYPE=Release",
    "-DSDL_ALSA=OFF",
    "-DSDL_HIDAPI_LIBUSB_SHARED=OFF",
    "-DSDL_JACK_SHARED=OFF",
    "-DSDL_KMSDRM_SHARED=OFF",
    "-DSDL_PIPEWIRE_SHARED=OFF",
    "-DSDL_PULSEAUDIO=OFF",
    "-DSDL_RPATH=OFF",
    "-DSDL_SNDIO=OFF",
    "-DSDL_WAYLAND_LIBDECOR_SHARED=OFF",
    "-DSDL_WAYLAND_SHARED=OFF",
    "-DSDL_X11_SHARED=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
    "ibus-devel",
    "libdecor-devel",
    "liburing-devel",
    "libusb-devel",
    "libx11-devel",
    "libxcursor-devel",
    "libxfixes-devel",
    "libxi-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "mesa-devel",
    "pipewire-devel",
    "pipewire-jack-devel",
    "wayland-devel",
]
depends = [
    # dynamically loaded
    "so:libGLESv2.so.2!libgles2",
    "so:libGL.so.1!libgl",
]
pkgdesc = "Simple DirectMedia Layer version 3"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://github.com/libsdl-org/SDL/releases/download/preview-{pkgver}/SDL3-{pkgver}.zip"
sha256 = "5ec43e84f8b1edb6412ed852ba547cb8c8a29ddde1a1b08097fed03bc7cdca1d"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3-devel")
def _(self):
    return self.default_devel()
