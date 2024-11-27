pkgname = "cava"
pkgver = "0.10.3"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/karlstav/cava"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "bf822ac18ae0ca2cf926c2875f3221591960c25f2bcab89ea19729be4b9c3663"


def post_install(self):
    self.install_license("LICENSE")
