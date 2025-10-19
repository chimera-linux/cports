pkgname = "cava"
pkgver = "0.10.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-input-alsa",
    "--disable-input-jack",
    "--disable-input-portaudio",
    "--disable-input-pulse",
    "--disable-input-sndio",
]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "autoconf-archive",
    "automake",
    "libtool",
    "pkgconf",
]
makedepends = [
    "fftw-devel",
    "iniparser-devel",
    "mesa-devel",
    "ncurses-devel",
    "pipewire-devel",
    "sdl2-compat-devel",
]
pkgdesc = "Console-based audio visualiser"
license = "MIT"
url = "https://github.com/karlstav/cava"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b1ce6653659a138cbaebf0ef2643a1569525559c597162e90bf9304ac8781398"


def post_install(self):
    self.install_license("LICENSE")
