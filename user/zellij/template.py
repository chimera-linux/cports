pkgname = "zellij"
pkgver = "0.41.2"
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
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://zellij.dev"
source = (
    f"https://github.com/zellij-org/zellij/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "12e7f0f80c1e39deed5638c4662fc070855cee0250a7eb1d76cefbeef8c2f376"
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
