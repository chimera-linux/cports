pkgname = "spotify-player"
pkgver = "0.25.2"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "pulseaudio-backend,streaming,media-control,image,sixel,notify,rustls-tls",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "cbindgen",
    "cmake",
    "pkgconf",
    "rust-bindgen",
]
makedepends = [
    "dbus-devel",
    "libpulse-devel",
    "libsixel-devel",
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "Spotify player in the terminal with full feature parity"
license = "MIT"
url = "https://github.com/aome510/spotify-player"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "60cc7cd60f66729039c0a48b134d8032c14817c88210d420722ad08340ad15cc"

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "spotify_player"))
    self.install_license("LICENSE")
