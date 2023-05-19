pkgname = "sdl"
pkgver = "2.26.5"
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
    "--disable-altivec",    # breaks C++ otherwise because of public altivec.h
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
    "dbus-devel", "udev-devel", "libusb-devel", "libsamplerate-devel",
    "glu-devel", "wayland-devel", "wayland-protocols", "libdecor-devel",
    "libxkbcommon-devel", "libxcursor-devel", "libxinerama-devel",
    "libxscrnsaver-devel", "libxrandr-devel", "libxi-devel", "libsm-devel",
    "vulkan-headers", "vulkan-loader", "mesa-devel", "pipewire-devel",
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
sha256 = "ad8fea3da1be64c83c45b1d363a6b4ba8fd60f5bde3b23ec73855709ec5eabf7"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel()

configure_gen = []
