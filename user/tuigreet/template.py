pkgname = "tuigreet"
pkgver = "0.9.1"
pkgrel = 2
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["greetd"]
pkgdesc = "Console greeter for greetd"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later"
url = "https://github.com/apognu/tuigreet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "14fd1fadeb84040eb31901da2b53a48aa55b0fdaccb36d96fa52ce2d2113667f"


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
