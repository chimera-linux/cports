pkgname = "zellij"
pkgver = "0.40.1"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "cargo"
# check fails because of wasm target
# https://github.com/zellij-org/zellij/blob/c25166c30af05a39f189c7520e3ab0e6a50905be/zellij-utils/src/consts.rs#L96
make_check_args = ["--release"]
hostmakedepends = ["cargo-auditable", "pkgconf", "go-md2man"]
makedepends = ["rust-std", "openssl-devel"]
pkgdesc = "Terminal workspace with batteries included"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://zellij.dev"
source = (
    f"https://github.com/zellij-org/zellij/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "1f0bfa13f2dbe657d76341a196f98a3b4caa47ac63abee06b39883a11ca220a8"
# generates completions with host bin
options = ["!cross"]


def post_build(self):
    with open(self.cwd / "docs/MANPAGE.md", "rb") as i:
        with open(self.cwd / "docs/zellij.1", "w") as o:
            self.do("go-md2man", input=i.read(), stdout=o)

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
    self.install_man("docs/zellij.1")
    self.install_license("LICENSE.md")

    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"assets/zellij.{shell}", shell)

    self.install_file("assets/logo.png", "usr/share/pixmaps", name="zellij.png")
    self.install_file("assets/zellij.desktop", "usr/share/applications")
