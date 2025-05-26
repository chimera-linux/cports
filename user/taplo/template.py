pkgname = "taplo"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "-p",
    "taplo-cli",
    "--no-default-features",
    "--features",
    "completions,native-tls,lsp",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "rust-std",
]
pkgdesc = "CLI for TOML"
license = "MIT"
url = "https://taplo.tamasfe.dev"
source = f"https://github.com/tamasfe/taplo/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c2f7b3234fc62000689a476b462784db4d1bb2be6edcc186654b211f691efaf8"
# generates completions with host binary
options = ["!cross"]


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


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"taplo.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/taplo",
                "completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_license("LICENSE")
    self.install_bin(f"target/{self.profile().triplet}/release/taplo")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"taplo.{shell}", shell)
