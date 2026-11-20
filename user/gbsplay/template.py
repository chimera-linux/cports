pkgname = "gbsplay"
pkgver = "0.0.104"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--mandir=/usr/share/man",
    # can't build shared libgbs for now, because some necessary files are not included in the tarball
    # SEE: https://github.com/mmitch/gbsplay/issues/42#issuecomment-6878566673
    # "--enable-sharedlibgbs",
    # "--with-xgbsplay",  # TODO: figure out how to explicitly split package…
    # --without-test just disables test *at build time* - tests will still run during check()
    "--without-test",
    # missing packages for plugouts: nas
    "--enable-alsa",
    "--disable-devdsp",  # OSS
    "--enable-pipewire",
    "--enable-pulse",
    "--enable-sdl",  # specifically SDL2
]
make_check_target = "test"
hostmakedepends = ["bash"]
makedepends = [
    "alsa-lib-devel",
    "libpulse-devel",
    "pipewire-devel",
    "sdl2-compat-devel",
]
pkgdesc = "Game Boy sound player"
license = "GPL-1.0-or-later"
url = "https://github.com/mmitch/gbsplay"
source = f"{url}/releases/download/{pkgver}/gbsplay-{pkgver}.tar.gz"
sha256 = "24d377046a774dd2bfa18e36afd7382d37a27715733954150b383a6a0ea4da06"
hardening = ["vis", "cfi"]  # sst fails


def post_install(self):
    self.install_completion("contrib/gbsplay.bashcompletion", "bash")
    self.install_completion("contrib/gbsplay.zshcompletion", "zsh")
