pkgname = "atuin"
pkgver = "18.2.0"
pkgrel = 0
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=client,server,sync,clipboard",
]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["sqlite-devel", "openssl-devel"]
pkgdesc = "Sync, search and backup tool for shell history"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "7fb87902ce09af2d29459e9158bc83c18519690d555259709cab40d9ee75b024"
# A bunch of failures yet to be investigated
# generates completions using host binary
options = ["!check", "!cross"]


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
