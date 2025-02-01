pkgname = "ruff"
pkgver = "0.9.4"
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
sha256 = "5d0a40ed9359b174e6b5420aae908a1120dbc631a62160916fd8dfff7a799e34"
# generates completions with host bin
# tests are mostly a waste of time
options = ["!cross", "!check"]

if self.profile().wordsize == 32:
    broken = "requires atomic64"


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
