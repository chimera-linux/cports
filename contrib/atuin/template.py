pkgname = "atuin"
pkgver = "18.1.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=client,server,sync,clipboard",
]
hostmakedepends = ["cargo", "pkgconf"]
makedepends = ["sqlite-devel", "openssl-devel"]
pkgdesc = "Sync, search and backup tool for shell history"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "17712bed6528a7f82cc1dffd56b7effe28270ee2f99247908d7a6adff9474338"
# A bunch of failures yet to be investigated
# generates completions using host binary
options = ["!check", "!cross"]


def do_prepare(self):
    # we patch Cargo.toml and Cargo.lock, so vendor after patch
    pass


def post_patch(self):
    from cbuild.util import cargo

    self.cargo.vendor()
    cargo.setup_vendor(self)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"atuin.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/atuin",
                "gen-completion",
                "--shell",
                shell,
                stdout=outf,
            )


def do_install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/atuin")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"atuin.{shell}", shell)
    self.install_license("LICENSE")
