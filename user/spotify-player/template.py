pkgname = "spotify-player"
pkgver = "0.22.1"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features",
    "pulseaudio-backend,streaming,media-control,image,sixel,notify",
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
sha256 = "b09ae88647758003eb7c666d3c2f60e1ff7624a14f9e8244332afe2b46167c4f"

if self.profile().wordsize == 32:
    broken = "needs atomic64"
elif self.profile().arch == "loongarch64":
    broken = "rustix/libc interaction garbage strikes again"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/spotify_player")
    self.install_license("LICENSE")
