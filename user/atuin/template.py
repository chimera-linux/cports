pkgname = "atuin"
pkgver = "18.10.0"
pkgrel = 1
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
make_build_args = ["--no-default-features"]
hostmakedepends = ["cargo-auditable", "protobuf-protoc", "pkgconf"]
makedepends = ["sqlite-devel", "openssl3-devel", "rust-std"]
pkgdesc = "Sync, search and backup tool for shell history"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "02228929976142f63b4464a35b8b29b29155e1814cf03e99c95381954c5d9e37"
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
        self.cargo.build(["--features=client,sync,clipboard,daemon"])

    for shell in ["bash", "fish", "nushell", "zsh"]:
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

    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"atuin.{shell}", shell)

    self.install_file(
        "crates/atuin-server/server.toml", "usr/share/examples/atuin"
    )

    # user daemon dinit service definition
    self.install_service(self.files_path / "atuin-daemon.user")

    self.install_license("LICENSE")


@subpackage("atuin-server")
def _(self):
    self.subdesc = "server"

    return [
        "usr/bin/atuin-server",
        "usr/share/examples",
    ]
