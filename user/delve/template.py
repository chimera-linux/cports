pkgname = "delve"
pkgver = "1.24.2"
pkgrel = 1
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
sha256 = "c26cce64c4cbef25b7652708cda198e9c081ea3abfbe411ed8048e131dba6275"


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
