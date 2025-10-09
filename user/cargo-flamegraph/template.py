# real flamegraph name is for the original perl project; this also has a cargo
# plugin
pkgname = "cargo-flamegraph"
pkgver = "0.6.9"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
depends = ["perf"]
pkgdesc = "Perf-based flamegraph generator"
license = "Apache-2.0 OR MIT"
url = "https://github.com/flamegraph-rs/flamegraph"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dd9b83affab5f9c1eaad0de9034037780e634c96fef4dce8fa83900e58cc240c"
# check: no tests
# cross: generates completions with host binary
options = ["!check", "!cross"]


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"flamegraph.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/flamegraph",
                "--completions",
                shell,
                stdout=f,
            )


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"flamegraph.{shell}", shell, "flamegraph")
    self.install_license("LICENSE-MIT")
