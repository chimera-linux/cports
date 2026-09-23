pkgname = "radicle"
pkgver = "1.10.3"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--bin",
    "rad",
    "--bin",
    "radicle-node",
    "--bin",
    "git-remote-rad",
    "--locked",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["libgit2-devel"]
depends = ["git", "openssh"]
pkgdesc = (
    "Decentralized git forge using a peer-to-peer and local-first approach"
)
license = "MIT AND Apache-2.0"
url = "https://radicle.dev"
source = f"https://seed.radicle.dev/raw/rad:z3gqcJUoA1n9HaHKufZs5FCSGazv5/archive/releases/{pkgver}>heartwood-releases-{pkgver}.tar.gz"
sha256 = "09a1ed99d6e57dbf8ec23a0d83f08f7fe7e1d848a714ca48387315689ff5b23d"
# the tests try to write to disk, but can't inside the container
options = ["!check"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "rad"))
    self.install_bin(cargo.target_path(self, "radicle-node"))
    self.install_bin(cargo.target_path(self, "git-remote-rad"))
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
