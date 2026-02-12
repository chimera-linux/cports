pkgname = "golangci-lint"
pkgver = "2.5.0"
pkgrel = 2
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0e0fcb42d9eda9ab0ff167c1df1e79cfe6aac72fbc9f97b9ff158c96baa438f4"
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
