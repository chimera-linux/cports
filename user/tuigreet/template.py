pkgname = "tuigreet"
pkgver = "0.9.1"
pkgrel = 2
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["greetd"]
pkgdesc = "Console greeter for greetd"
license = "GPL-3.0-or-later"
url = "https://github.com/apognu/tuigreet"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "14fd1fadeb84040eb31901da2b53a48aa55b0fdaccb36d96fa52ce2d2113667f"


def pre_prepare(self):
    # the version that is in there is busted on loongarch
    self.do(
        "cargo",
        "update",
        "--package",
        "libc",
        "--precise",
        "0.2.170",
        allow_network=True,
    )


def post_install(self):
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
