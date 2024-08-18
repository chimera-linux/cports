pkgname = "cava"
pkgver = "0.10.2"
pkgrel = 2
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
sha256 = "853ee78729ed3501d0cdf9c1947967ad3bfe6526d66a029b4ddf9adaa6334d4f"


def post_install(self):
    self.install_license("LICENSE")
