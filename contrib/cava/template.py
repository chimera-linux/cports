pkgname = "cava"
pkgver = "0.10.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-input-alsa",
    "--disable-input-portaudio",
    "--disable-input-pulse",
    "--disable-input-sndio",
]
configure_gen = ["./autogen.sh"]
make_dir = "."
hostmakedepends = [
    "autoconf",
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
    "sdl-devel",
]
pkgdesc = "Console-based audio visualiser"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://github.com/karlstav/cava"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a3a60814326fa34b54e93ce0b1e66460d55f1007e576c5152fd47024d9ceaff9"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
