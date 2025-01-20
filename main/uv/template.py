pkgname = "uv"
pkgver = "0.5.21"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zlib-ng-compat-devel",
    "zstd-devel",
]
pkgdesc = "Python package installer"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/astral-sh/uv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a7de0acb9fcdb4dce09d2d16397c91b30cbf653ceeacc30b250df42c9154edbe"
# too many of them need net
# completions with host bin
options = ["!check", "!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    for shell in ["bash", "fish", "nushell", "zsh"]:
        with open(self.cwd / f"uv.{shell}", "w") as cf:
            self.do(
                f"./target/{self.profile().triplet}/release/uv",
                "--generate-shell-completion",
                shell,
                stdout=cf,
            )
        with open(self.cwd / f"uvx.{shell}", "w") as cf:
            self.do(
                f"./target/{self.profile().triplet}/release/uvx",
                "--generate-shell-completion",
                shell,
                stdout=cf,
            )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def post_install(self):
    self.install_license("LICENSE-MIT")
    for shell in ["bash", "fish", "nushell", "zsh"]:
        self.install_completion(f"uv.{shell}", shell)
        self.install_completion(f"uvx.{shell}", shell, "uvx")
