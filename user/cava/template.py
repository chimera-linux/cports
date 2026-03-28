pkgname = "cava"
pkgver = "0.10.7"
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
sha256 = "43f994f7e609fab843af868d8a7bc21471ac62c5a4724ef97693201eac42e70a"


def post_install(self):
    self.install_license("LICENSE")
