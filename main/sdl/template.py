pkgname = "sdl"
pkgver = "2.28.4"
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
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "nasm", "wayland-progs"]
makedepends = [
    "dbus-devel",
    "udev-devel",
    "libusb-devel",
    "libsamplerate-devel",
    "glu-devel",
    "wayland-devel",
    "wayland-protocols",
    "libdecor-devel",
    "libxkbcommon-devel",
    "libxcursor-devel",
    "libxinerama-devel",
    "libxscrnsaver-devel",
    "libxrandr-devel",
    "libxi-devel",
    "libsm-devel",
    "vulkan-headers",
    "vulkan-loader-devel",
    "mesa-devel",
    "pipewire-devel",
]
depends = [
    # dynamically loaded
    "so:libGLESv2.so.2!libgles2",
    "so:libGL.so.1!libgl",
]
pkgdesc = "Simple DirectMedia Layer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://www.libsdl.org/release/SDL2-{pkgver}.tar.gz"
sha256 = "888b8c39f36ae2035d023d1b14ab0191eb1d26403c3cf4d4d5ede30e66a4942c"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()


configure_gen = []
