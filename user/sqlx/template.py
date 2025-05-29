pkgname = "sqlx"
pkgver = "0.8.6"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "-p",
    "sqlx-cli",
    "--no-default-features",
    "--features=native-tls,postgres,sqlite-unbundled,completions",
]
make_check_args = [*make_build_args]
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "openssl3-devel",
    "rust-std",
    "sqlite-devel",
]
pkgdesc = "Rust sql toolkit cli utility"
license = "Apache-2.0 OR MIT"
url = "https://github.com/launchbadge/sqlx"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "75d0b4d1f3081a877c7b75936f069f9327bb2ceb4dc206f5a7fc89e0cd9bc31e"
# generates completions with host binary
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"sqlx.{shell}", "w") as outf:
            self.do(
                f"target/{self.profile().triplet}/release/sqlx",
                "completions",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/sqlx")
    self.install_bin(f"target/{self.profile().triplet}/release/cargo-sqlx")
    self.install_license("LICENSE-MIT")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"sqlx.{shell}", shell)
