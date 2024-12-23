pkgname = "ruff"
pkgver = "0.8.4"
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
maintainer = "triallax <triallax@tutanota.com>"
license = "MIT"
url = "https://docs.astral.sh/ruff"
source = f"https://github.com/astral-sh/ruff/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f48c9e2479e72957ce5dfd3d0cc9d27f5aeb36d15ae2f97c9c116fc5c742dc5d"
# generates completions with host bin
# tests are mostly a waste of time
options = ["!cross", "!check"]


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
