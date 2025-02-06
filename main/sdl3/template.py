pkgname = "sdl3"
pkgver = "3.2.2"
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
    "-DSDL_ALTIVEC=OFF",  # ppc64le fail in sdl2-compat blit tests
    "-DSDL_IBUS=OFF",  # causes depcycles for ffmpeg, fluidsynth, etc.
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "dbus-devel",
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
    "so:libGLESv2.so.2!mesa-gles2-libs",
    "so:libGL.so.1!mesa-gl-libs",
]
pkgdesc = "Simple DirectMedia Layer version 3"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://github.com/libsdl-org/SDL/releases/download/release-{pkgver}/SDL3-{pkgver}.zip"
sha256 = "58d8adc7068d38923f918e0bdaa9c4948f93d9ba204fe4de8cc6eaaf77ad6f82"


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl3-devel-static")
def _(self):
    self.subdesc = "static libraries"

    return ["usr/lib/*.a"]


@subpackage("sdl3-devel")
def _(self):
    # cmake dependencies shenanigans
    self.depends += [self.with_pkgver("sdl3-devel-static")]

    return self.default_devel()
