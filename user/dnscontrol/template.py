pkgname = "dnscontrol"
pkgver = "4.17.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e126665a00eb0a7983ed2dd5a61ac84d597e3e8016fc010d2bac7f1bbe90d201"
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
