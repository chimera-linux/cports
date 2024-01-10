pkgname = "i3status-rust"
pkgver = "0.32.3"
pkgrel = 0
build_style = "cargo"
# Enable the notmuch feature
make_build_args = ["--features=notmuch"]
make_install_args = ["--features=notmuch"]
make_check_args = ["--features=notmuch"]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = [
    "libpulse-devel",
    "libsensors-devel",
    "notmuch-devel",
    "openssl-devel",
    "rust-std",
]
pkgdesc = "Feature-rich status bar generator"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-only"
url = "https://github.com/greshake/i3status-rust"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6a2c37d0e424d666f297d7ec36279b54a522acf5bf77af883be1991513e4da61"


def post_install(self):
    self.install_license("LICENSE")
    self.install_files("files/icons", f"usr/share/{pkgname}")
    self.install_files("files/themes", f"usr/share/{pkgname}")
