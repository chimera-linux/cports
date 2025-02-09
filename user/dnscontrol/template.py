pkgname = "dnscontrol"
pkgver = "4.16.0"
pkgrel = 1
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ce9aa8887a8cad28b17f8e07f0755730beadae70f48976116ad8be7390cec3a6"
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
