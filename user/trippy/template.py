pkgname = "trippy"
pkgver = "0.13.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--bin", "trip"]
make_build_args = [*make_build_args]
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Network diagnostic tool combining traceroute and ping"
license = "Apache-2.0"
url = "https://trippy.rs"
source = (
    f"https://github.com/fujiapple852/trippy/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "72e598d2e0b947e8bc46706021c511f169b7e7634a734c326e492e0f30725c35"
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
