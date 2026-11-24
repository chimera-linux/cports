pkgname = "ardour"
pkgver = "9.10.0"
pkgrel = 0
build_style = "waf"
configure_args = [
    "--configdir=/etc",
    "--cxx17",
    "--freedesktop",
    "--keepflags",
    "--no-phone-home",
    "--optimize",
    "--with-backends=pulseaudio,jack,dummy",
]
hostmakedepends = [
    "gettext",
    "itstool",
    "perl",
    "pkgconf",
    "python",
]
makedepends = [
    "alsa-lib-devel",
    "aubio-devel",
    "boost-devel",
    "cairomm1.0-devel",
    "fftw-devel",
    "fluidsynth-devel",
    "glibmm2.4-devel",
    "hidapi-devel",
    "libarchive-devel",
    "libedit-readline-devel",
    "libjpeg-turbo-devel",
    "liblo-devel",
    "libpng-devel",
    "libpulse-devel",
    "libsamplerate-devel",
    "libsndfile-devel",
    "libusb-devel",
    "lilv-devel",
    "lrdf-devel",
    "lv2",
    "pango-devel",
    "pangomm1.4-devel",
    "pipewire-jack-devel",
    "redland-devel",
    "rubberband-devel",
    "serd-devel",
    "sratom-devel",
    "suil-devel",
    "taglib-devel",
    "vamp-plugin-sdk-devel",
]
pkgdesc = "Digital audio workstation"
license = "GPL-2.0-or-later AND CC0-1.0 AND MIT"
url = "https://ardour.org"
source = f"https://community.ardour.org/src/Ardour-{pkgver}.tar.bz2"
sha256 = "8d534a957c724aa8eca5802b225ca4ca19b63243573cb6891287b64e33b34c76"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["!int"]
# bundled stuff
options = ["etcfiles", "!cross", "!scanshlibs"]
exec_wrappers = [("/usr/bin/clang-cpp", "cpp")]


if self.profile.endian == "big":
    broken = "busted audio stuff"


def check(self):
    self.do("python", "waf", "test")


def post_install(self):
    self.rename("usr/share/appdata", "metainfo")
    self.uninstall("usr/lib/ardour9/*.a", glob=True)
    self.install_license("COPYING")
