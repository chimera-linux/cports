pkgname = "i3status-rust"
pkgver = "0.34.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=icu_calendar,maildir,notmuch,pipewire,pulseaudio",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = [
    "curl-devel",
    "dbus-devel",
    "libpulse-devel",
    "lm-sensors-devel",
    "notmuch-devel",
    "openssl3-devel",
    "pipewire-devel",
    "rust-std",
]
pkgdesc = "Generates content on bars that support the i3bar protocol"
license = "GPL-3.0-only"
url = "https://github.com/greshake/i3status-rust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6787174f749f15e9e177a7730f6abeae05de2b156922f6d02e512b31f35d1d17"

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/i3status-rs")
    self.install_files("files", "usr/share", name="i3status-rust")
