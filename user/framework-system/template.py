pkgname = "framework-system"
pkgver = "0.6.5"
pkgrel = 0
archs = ["x86_64"]
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "linux-headers",
    "udev-devel",
]
pkgdesc = "Command line tools for Framework computers"
license = "BSD-3-Clause"
url = "https://github.com/FrameworkComputer/framework-system"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "51daef8eac68f3c8b69956f0250a2a4029243a5631a8ee9a537f6d4db730a890"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/framework_tool")
    self.install_completion(
        "framework_tool/completions/bash/framework_tool",
        "bash",
        name="framework_tool",
    )
    self.install_completion(
        "framework_tool/completions/fish/framework_tool.fish",
        "fish",
        name="framework_tool",
    )
    self.install_completion(
        "framework_tool/completions/zsh/_framework_tool",
        "zsh",
        name="framework_tool",
    )
    self.install_license("LICENSE.md")
