pkgname = "atuin"
pkgver = "18.16.0"
pkgrel = 0
build_style = "cargo"
# we patch Cargo.toml and Cargo.lock
prepare_after_patch = True
make_build_args = [
    "--no-default-features",
    "--features=client,sync,clipboard,daemon,hex",
]
hostmakedepends = ["cargo-auditable", "protobuf-protoc", "pkgconf"]
makedepends = ["sqlite-devel", "openssl3-devel", "rust-std"]
pkgdesc = "Sync, search and backup tool for shell history"
license = "MIT"
url = "https://github.com/atuinsh/atuin"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "433a6ee912d84b2aa4b59b329775a7ee1a1cdc3094412c2f185ac5ce681a64f0"
# A bunch of failures yet to be investigated
# generates completions using host binary
options = ["!check", "!cross"]

# TODO service + sysusers


def post_build(self):
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

    self.install_license("LICENSE")


@subpackage("atuin-server")
def _(self):
    self.subdesc = "server"

    return [
        "usr/bin/atuin-server",
        "usr/share/examples",
    ]
