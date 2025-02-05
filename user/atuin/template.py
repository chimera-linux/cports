pkgname = "atuin"
pkgver = "18.4.0"
pkgrel = 2
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
make_build_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable", "protobuf-protoc", "pkgconf"]
makedepends = ["sqlite-devel", "openssl3-devel", "rust-std"]
pkgdesc = "Sync, search and backup tool for shell history"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "de6d2bcf10de4d757916c7e92a70f15929fc1dea75abc4df09b0baedf26a53b2"
# A bunch of failures yet to be investigated
# generates completions using host binary
options = ["!check", "!cross"]

# TODO service + sysusers


def build(self):
    tgt_base = f"target/{self.profile().triplet}/release"

    with self.stamp("server"):
        self.cargo.build(["--features=server"])
        self.mv(f"{tgt_base}/atuin", f"{tgt_base}/atuin-server")

    with self.stamp("client"):
        self.cargo.build(["--features=client,sync,clipboard"])

    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"atuin.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/atuin",
                "gen-completion",
                "--shell",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/atuin")
    self.install_bin(f"target/{self.profile().triplet}/release/atuin-server")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"atuin.{shell}", shell)

    self.install_file(
        "crates/atuin-server/server.toml", "usr/share/examples/atuin"
    )

    self.install_license("LICENSE")


@subpackage("atuin-server")
def _(self):
    self.subdesc = "server"

    return [
        "usr/bin/atuin-server",
        "usr/share/examples",
    ]
