pkgname = "stash"
pkgver = "0.4.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "sqlite-devel", "turnstile"]
provides = [
    "cmd:stash",
    "stash-copy",
    "stash-paste",
    "cmd:wl-copy",
    "cmd:wl-paste",
]
pkgdesc = "Lightweight wayland clipboard manager with persistent history"
license = "MPL-2.0"
url = "https://github.com/notashelf/stash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c962f634537433d302b5ed85a2bd9cf6915e218d3ec335710b3e529a222efd27"


def post_install(self):
    self.install_link("usr/bin/stash-copy", "stash")
    self.install_link("usr/bin/stash-paste", "stash")
    self.install_link("usr/bin/wl-copy", "stash")
    self.install_link("usr/bin/wl-paste", "stash")
    self.install_service(self.files_path / "stash.user")
