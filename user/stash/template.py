pkgname = "stash"
pkgver = "0.3.5"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["sqlite-devel", "turnstile"]
provides = ["cmd:stash"]
pkgdesc = "Lightweight wayland clipboard manager with persistent history"
license = "MPL-2.0"
url = "https://github.com/notashelf/stash"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e35a07ef150eca8ae4ae78d421e8861850a33c265cda0d6bdc52f63b2fbea492"


def post_install(self):
    self.install_service(self.files_path / "stash.user")
