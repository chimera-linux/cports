pkgname = "dnscontrol"
pkgver = "4.15.4"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ef78e1c5fb84e13ba6ea80e9de4754ea89c5b756a445aec8b28d8ce65996f4f1"
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
