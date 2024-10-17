pkgname = "ruff"
pkgver = "0.7.0"
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
    "zstd-devel",
]
depends = ["python"]
pkgdesc = "Python formatter and linter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://docs.astral.sh/ruff"
source = f"https://github.com/astral-sh/ruff/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1bb27c8b7da3d2d2a676c677692f9a527d5fa5697a52c0515f9662f735449293"
# generates completions with host bin
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        with open(self.cwd / f"ruff.{shell}", "w") as f:
            self.do(
                f"./target/{self.profile().triplet}/release/ruff",
                "generate-shell-completion",
                shell,
                stdout=f,
            )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check(args=["--workspace", "--exclude", "ruff_benchmark"])


def post_install(self):
    for shell in ["bash", "fish", "zsh", "nushell"]:
        self.install_completion(f"ruff.{shell}", shell)
    self.install_license("LICENSE")
