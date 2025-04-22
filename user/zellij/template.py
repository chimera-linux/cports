pkgname = "zellij"
pkgver = "0.42.2"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
# check fails because of wasm target
# https://github.com/zellij-org/zellij/blob/c25166c30af05a39f189c7520e3ab0e6a50905be/zellij-utils/src/consts.rs#L96
make_build_args = ["--no-default-features", "--features=plugins_from_target"]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args, "--release"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["curl-devel", "rust-std", "zstd-devel"]
pkgdesc = "Terminal workspace with batteries included"
license = "MIT"
url = "https://zellij.dev"
source = (
    f"https://github.com/zellij-org/zellij/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "f1cd4b36775dd367b839e394b54e91042b0cd0f2b9e0901b1dec8517ff3929c0"
# generates completions with host bin
options = ["!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"assets/zellij.{shell}", "w") as o:
            self.do(
                f"target/{self.profile().triplet}/release/zellij",
                "setup",
                "--generate-completion",
                shell,
                stdout=o,
            )


def post_install(self):
    self.install_license("LICENSE.md")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"assets/zellij.{shell}", shell)

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="zellij.png")
    self.install_file("assets/zellij.desktop", "usr/share/applications")
