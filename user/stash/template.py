pkgname = "stash"
pkgver = "0.5.2"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std", "sqlite-devel", "turnstile"]
pkgdesc = "Wayland clipboard manager with persistent history"
license = "MPL-2.0"
url = "https://github.com/notashelf/stash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "284315c853e1135ec671416416b7279881d8bfd8ff74b541a49dc5da5b925825"


def post_install(self):
    self.install_link("usr/bin/stash-copy", "stash")
    self.install_link("usr/bin/stash-paste", "stash")
    self.install_link("usr/bin/wl-copy", "stash")
    self.install_link("usr/bin/wl-paste", "stash")
    self.install_service(self.files_path / "stash.user")
