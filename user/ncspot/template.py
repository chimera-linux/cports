pkgname = "ncspot"
pkgver = "1.3.2"
pkgrel = 1
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python",
]
makedepends = [
    "dbus-devel",
    "libpulse-devel",
    "libxcb-devel",
    "ncurses-devel",
    "openssl3-devel"
]
pkgdesc = "Cross-platform ncurses Spotify client written in Rust"
license = "BSD-2-Clause"
url = "https://github.com/hrkfdn/ncspot"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "d60c04c027dddbc57cbd9bcb23ec4967b4ae7330a280a7a5f6b77c1ea2cf8c99"

def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/{pkgname}")
    self.install_file("misc/ncspot.desktop", "usr/share/applications")
    self.install_file("images/logo.svg", f"usr/share/icons/hicolor/scalable/apps", 0o644, f"{pkgname}.svg")
    self.install_license("LICENSE")
