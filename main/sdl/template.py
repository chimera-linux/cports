pkgname = "sdl"
pkgver = "2.30.0"
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
sha256 = "36e2e41557e0fa4a1519315c0f5958a87ccb27e25c51776beb6f1239526447b0"
# no check target
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("sdl-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()


configure_gen = []
