pkgname = "delve"
pkgver = "1.24.0"
pkgrel = 0
# supported archs
archs = ["aarch64", "x86_64"]
build_style = "go"
make_build_args = ["./cmd/dlv/..."]
make_check_args = [*make_build_args]
hostmakedepends = ["go"]
pkgdesc = "Debugger for the Go programming language"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://github.com/go-delve/delve"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "940fc50d6338dfe515982ac5fcc3247616f23e2652048ac4f2b439ebd51741c1"


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"delve.{shell}", "w") as outf:
            self.do(
                "./build/dlv",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    self.install_license("LICENSE")
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"delve.{shell}", shell, "dlv")
