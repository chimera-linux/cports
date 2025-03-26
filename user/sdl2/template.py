pkgname = "sdl2"
pkgver = "2.32.2"
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
    "so:libGLESv2.so.2!mesa-gles2-libs",
    "so:libGL.so.1!mesa-gl-libs",
]
# transitional
provides = [self.with_pkgver("sdl")]
pkgdesc = "Simple DirectMedia Layer"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://www.libsdl.org/release/SDL2-{pkgver}.tar.gz"
sha256 = "c5f30c427fd8107ee4a400c84d4447dd211352512eaf0b6e89cc6a50a2821922"
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
