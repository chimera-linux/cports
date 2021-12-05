pkgname = "sdl"
pkgver = "2.0.18"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-rpath",
    "--disable-alsa",
    "--disable-esd",
    "--disable-nas",
    "--disable-oss",
    "--disable-pulseaudio", # TODO: maybe enable later?
    "--disable-pipewire",   # TODO: enable later
    "--disable-sndio",      # TODO: enable later
    "--disable-altivec",    # breaks C++ otherwise because of public altivec.h
    "--disable-x11-shared",
    "--disable-pulseaudio-shared",
    "--disable-pipewire-shared",
    "--disable-wayland-shared",
    "--enable-dbus",
    "--enable-libudev",
    "--enable-libdecor",
    "--enable-video-opengl",
    "--enable-video-opengles",
    "--enable-video-vulkan",
    "--enable-video-wayland",
    "--enable-video-x11-xinput",
    "--enable-video-x11-xcursor",
    "--enable-video-x11-xrandr",
    "--enable-video-x11-xinerama",
    "--enable-video-x11-scrnsaver",
    "--enable-video-x11-xshape",
    "--enable-video-x11-vm",
    "--enable-clock_gettime",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "nasm", "wayland-progs"]
makedepends = [
    "dbus-devel", "eudev-devel", "libusb-devel", "libsamplerate-devel",
    "glu-devel", "wayland-devel", "wayland-protocols", "libdecor-devel",
    "libxcursor-devel", "libxinerama-devel", "libxscrnsaver-devel",
    "libxrandr-devel", "libxi-devel", "libsm-devel", "vulkan-headers",
    "vulkan-loader", "mesa-devel",
    #"libpulse-devel",
    #"pipewire-devel",
    #"sndio-devel",
]
depends = [
    # dynamically loaded
    "so:libGLESv2.so.2",
    "so:libGL.so.1",
]
depends_providers = {
    "so:libGLESv2.so.2": "libgles2",
    "so:libGL.so.1": "libgl",
}
pkgdesc = "Simple DirectMedia Layer"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Zlib"
url = "https://libsdl.org"
source = f"https://www.libsdl.org/release/SDL2-{pkgver}.tar.gz"
sha256 = "94d40cd73dbfa10bb6eadfbc28f355992bb2d6ef6761ad9d4074eff95ee5711c"
# no check target
options = ["!check"]

def post_install(self):
    self.install_license("LICENSE.txt")

@subpackage("sdl-static")
def _static(self):
    return self.default_static()

@subpackage("sdl-devel")
def _devel(self):
    self.depends += makedepends

    return self.default_devel(extra = ["usr/share"])
