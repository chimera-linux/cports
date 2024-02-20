pkgname = "i3status-rust"
pkgver = "0.33.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--features=notmuch"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "dbus-devel",
    "libcurl-devel",
    "libpulse-devel",
    "libsensors-devel",
    "notmuch-devel",
    "openssl-devel",
]
pkgdesc = "Generates content on bars that support the i3bar protocol"
maintainer = "ttyyls <contact@behri.org>"
license = "GPL-3.0-only"
url = "https://github.com/greshake/i3status-rust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "fd722f630080ef0b25558bec9b342a9fe8842c3af049d55a1370c6760ad84c67"


def post_install(self):
    self.install_files("files", "usr/share", name="i3status-rust")
