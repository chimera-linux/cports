pkgname = "golangci-lint"
pkgver = "2.2.2"
pkgrel = 0
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "807175564d9f641365677a62e5ea50b41c05e6d8204fc8225492a25a26551189"
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
