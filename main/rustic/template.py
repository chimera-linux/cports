pkgname = "rustic"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cargo"
make_build_args = ["--no-default-features", "--features=webdav,tui"]
make_install_args = [*make_build_args]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "zstd-devel"]
pkgdesc = "Encrypted and deduplicated backups - restic compatible"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "Apache-2.0 OR MIT"
url = "https://rustic.cli.rs"
source = (
    f"https://github.com/rustic-rs/rustic/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "b911515ce3879f6d2dbd179014ccbad7b157152ff28ecb7812ca6ea65a315523"
# generates completions with host bins
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"rustic.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/rustic",
                "completions",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"rustic.{shell}", shell)
    self.install_license("LICENSE-MIT")
