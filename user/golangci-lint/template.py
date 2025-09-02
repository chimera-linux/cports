pkgname = "golangci-lint"
pkgver = "2.4.0"
pkgrel = 0
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ac90b9f5343f4b18b1b477303c104fb1537d63260862e264d31a144a9685f81b"
# cross: generates completions with host binary
# some tests fail because of chroot and some need network
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"golangci.{shell}", "w") as outf:
            self.do(
                "build-cccc/golangci-lint",
                "completion",
                shell,
                stdout=outf,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"golangci.{shell}", shell)
