pkgname = "zellij"
pkgver = "0.43.1"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
# check fails because of wasm target
# https://github.com/zellij-org/zellij/blob/c25166c30af05a39f189c7520e3ab0e6a50905be/zellij-utils/src/consts.rs#L96
make_build_args = [
    "--no-default-features",
    "--features=plugins_from_target,web_server_capability",
]
make_install_args = [*make_build_args]
make_check_args = [*make_build_args, "--release"]
hostmakedepends = ["cargo-auditable", "cmake", "pkgconf", "rust-bindgen"]
makedepends = ["curl-devel", "rust-std", "sqlite-devel", "zstd-devel"]
pkgdesc = "Terminal workspace with batteries included"
license = "MIT"
url = "https://zellij.dev"
source = (
    f"https://github.com/zellij-org/zellij/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "e9fd24190869be6e9e8d731df2ccd0b3b1dd368ae9dbb9d620ec905b83e325ec"
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
