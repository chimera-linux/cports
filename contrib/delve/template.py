pkgname = "delve"
pkgver = "1.23.0"
pkgrel = 3
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
sha256 = "fed613f0457600a30713968c111bb1fc3b014a4ebb25acaaf45cdbd03f8337a1"


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
