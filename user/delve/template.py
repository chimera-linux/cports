pkgname = "delve"
pkgver = "1.27.1"
pkgrel = 0
# supported archs
archs = ["aarch64", "x86_64"]
build_style = "go"
make_build_args = ["./cmd/dlv/..."]
make_check_args = [*make_build_args]
hostmakedepends = ["go"]
pkgdesc = "Debugger for the Go programming language"
license = "MIT"
url = "https://github.com/go-delve/delve"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dca9ec6f2c392a00449ad748b3a229e92ba4efa67f4e7582f2cc45974429928f"
# cross: generates completions with host binary
options = ["!cross"]


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
