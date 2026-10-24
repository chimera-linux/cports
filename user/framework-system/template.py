pkgname = "framework-system"
pkgver = "0.6.6"
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
sha256 = "5d285d508cc5b2d1df2d9573dda4a4e6118f1b16a5dcc24e50fc078995e3bb29"


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
