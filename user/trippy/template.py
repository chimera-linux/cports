pkgname = "trippy"
pkgver = "0.12.2"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "trip"]
make_build_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Network diagnostic tool combining traceroute and ping"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://trippy.rs"
source = (
    f"https://github.com/fujiapple852/trippy/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "6f23549e5f398113ecd0d2f15c829f5ab84fcdf99dde9942c61746e72f990085"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"trip.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/trip",
                "--generate",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/trip")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"trip.{shell}", shell, name="trip")
