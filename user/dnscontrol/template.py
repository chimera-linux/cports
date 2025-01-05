pkgname = "dnscontrol"
pkgver = "4.15.3"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c0322bd15392b28d18e76ffa148a2b8d4ae5923caab724fa89c3c08abc39964e"
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
