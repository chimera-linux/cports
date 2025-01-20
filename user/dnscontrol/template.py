pkgname = "dnscontrol"
pkgver = "4.15.5"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "baaf10cd3dd100b6676ae0f8a0b9fabc16b8971403a039ef2fa79a265ec600ba"
# tests rely on network
# generates completions with host bins
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "zsh"]:
        with open(self.cwd / f"dnscontrol.{shell}", "w") as outf:
            self.do(
                "build/dnscontrol",
                "shell-completion",
                shell,
                stdout=outf,
            )


def install(self):
    self.install_bin("build/dnscontrol")
    self.install_license("LICENSE")
    for shell in ["bash", "zsh"]:
        self.install_completion(f"dnscontrol.{shell}", shell)
