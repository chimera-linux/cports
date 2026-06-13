pkgname = "framework-system"
pkgver = "0.6.4"
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
sha256 = "7c1a717651f879bc921f3789046f056752b211630b4585696c2dd1ca7e037b9b"


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
