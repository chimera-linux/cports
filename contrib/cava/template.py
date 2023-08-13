pkgname = "cava"
pkgver = "0.9.1"
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
source = f"https://github.com/karlstav/cava/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "483f571d5fba5fb8aa81511c4dcf8ce0949c7c503ec6c743c2914cd78e6faf03"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
