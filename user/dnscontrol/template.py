pkgname = "dnscontrol"
pkgver = "5.7.0"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "System for maintaining DNS zones"
license = "MIT"
url = "https://dnscontrol.org"
source = f"https://github.com/StackExchange/dnscontrol/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "4a76b675ba797cf9ee3200c33c0452fd74da429b93b32bd4a56e00307ca4d6ef"
hardening = []
# tests rely on network
# generates completions with host bins
options = ["!check", "!cross"]

match self.profile.arch:
    case "ppc64le" | "ppc64":
        # https://github.com/golang/go/issues/82324
        hardening += ["!pie"]


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
