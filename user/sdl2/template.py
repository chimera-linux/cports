pkgname = "sdl2"
pkgver = "2.32.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-alsa",
    "--disable-esd",
    "--disable-nas",
    "--disable-oss",
    "--disable-pulseaudio",
    "--disable-sndio",
    "--disable-altivec",  # breaks C++ otherwise because of public altivec.h
    "--disable-x11-shared",
    "--disable-pulseaudio-shared",
    "--disable-pipewire-shared",
    "--disable-wayland-shared",
    "--enable-dbus",
    "--enable-libudev",
    "--enable-libdecor",
    "--enable-pipewire",
    "--enable-video-opengl",
    "--enable-video-opengles",
    "--enable-video-vulkan",
    "--enable-video-wayland",
    "--enable-clock_gettime",
]
configure_gen = []
hostmakedepends = ["pkgconf", "nasm", "wayland-progs"]
makedepends = [
    "dbus-devel",
    "glu-devel",
    "libdecor-devel",
    "libsamplerate-devel",
    "libsm-devel",
    "libusb-devel",
    "libxcursor-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxkbcommon-devel",
    "libxrandr-devel",
    "libxscrnsaver-devel",
    "mesa-devel",
    "pipewire-devel",
    "udev-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "wayland-devel",
    "wayland-protocols",
]
depends = [
    "so:libGL.so.1!mesa-gl-libs",
    # dynamically loaded
    "so:libGLESv2.so.2!mesa-gles2-libs",
]
# transitional
provides = [self.with_pkgver("sdl")]
pkgdesc = "Simple DirectMedia Layer"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://www.libsdl.org/release/SDL2-{pkgver}.tar.gz"
sha256 = "5f5993c530f084535c65a6879e9b26ad441169b3e25d789d83287040a9ca5165"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl2-devel")
def _(self):
    self.depends += makedepends
    # transitional
    self.provides = [self.with_pkgver("sdl-devel")]

    return self.default_devel()
