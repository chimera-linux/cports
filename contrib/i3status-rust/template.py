pkgname = "i3status-rust"
pkgver = "0.32.3"
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
sha256 = "6a2c37d0e424d666f297d7ec36279b54a522acf5bf77af883be1991513e4da61"


def post_install(self):
    self.install_files("files", "usr/share", name="i3status-rust")
