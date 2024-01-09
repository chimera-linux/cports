pkgname = "cava"
pkgver = "0.10.0"
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
sha256 = "1e40c93cb476ada538c131cb68ab1b56ce214d75b834508cbe76a57ae1ea153f"
hardening = ["vis", "cfi"]


def post_install(self):
    self.install_license("LICENSE")
