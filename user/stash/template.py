pkgname = "stash"
pkgver = "0.3.6"
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
sha256 = "fda98e39e9ce5dc352299190173db20aac91588648ddd67e872ba811156eda99"


def post_install(self):
    self.install_link("usr/bin/stash-copy", "stash")
    self.install_link("usr/bin/stash-paste", "stash")
    self.install_link("usr/bin/wl-copy", "stash")
    self.install_link("usr/bin/wl-paste", "stash")
    self.install_service(self.files_path / "stash.user")
