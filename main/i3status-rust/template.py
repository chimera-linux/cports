pkgname = "i3status-rust"
pkgver = "0.33.2"
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
    "dbus-devel",
    "libcurl-devel",
    "libpulse-devel",
    "libsensors-devel",
    "notmuch-devel",
    "openssl-devel",
    "pipewire-devel",
    "rust-std",
]
pkgdesc = "Generates content on bars that support the i3bar protocol"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://github.com/greshake/i3status-rust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "eb9df6eac57a65a7948ba763a7d1fcef5d506e374a4ac9d57aa88a22270ee06b"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/i3status-rs")
    self.install_files("files", "usr/share", name="i3status-rust")
