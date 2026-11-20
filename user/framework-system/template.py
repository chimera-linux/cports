pkgname = "framework-system"
pkgver = "0.6.7"
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
sha256 = "be7e31266dd09d5838507eeff61cc5174b2bc97e6ae18be27c82fc7c91ecb537"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "framework_tool"))
    self.install_man("framework_tool/framework_tool.1")
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
