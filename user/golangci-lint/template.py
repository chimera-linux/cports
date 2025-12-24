pkgname = "golangci-lint"
pkgver = "2.7.2"
pkgrel = 0
build_style = "go"
make_dir = "build-cccc"
make_build_args = ["./cmd/golangci-lint"]
hostmakedepends = ["go"]
pkgdesc = "Linters runner for Go"
license = "GPL-3.0-or-later"
url = "https://golangci-lint.run"
source = f"https://github.com/golangci/golangci-lint/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cb4a499cf99e67660fafb5a3a91dd0703151ba48c0891953ffb7c365f13f35e2"
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
