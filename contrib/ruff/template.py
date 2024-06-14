pkgname = "ruff"
pkgver = "0.4.9"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = [
    "rust-std",
    "zstd-devel",  # checks only
]
depends = ["python"]
pkgdesc = "Python formatter and linter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://docs.astral.sh/ruff"
source = f"https://github.com/astral-sh/ruff/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "815c5b9b316a4d72dc526c6b4b2421df708556294af514e6fe25ff99722d36e3"
# generates completions with host bin
options = ["!cross"]


if self.profile().arch == "riscv64":
    broken = "runs for hours, uses 100GB memory, dies"


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)

    # TODO: our cargo vendor does not take into account custom source entries
    # (this is spat out by `cargo vendor`)
    with open(
        f"{self.builddir}/{pkgname}-{pkgver}/.cargo/config.toml", "a"
    ) as f:
        f.write(
            """
[source."git+https://github.com/astral-sh/lsp-types.git?rev=3512a9f"]
git = "https://github.com/astral-sh/lsp-types.git"
rev = "3512a9f"
replace-with = "vendored-sources"
[source."git+https://github.com/salsa-rs/salsa.git?rev=05b4e3ebdcdc47730cdd359e7e97fb2470527279"]
git = "https://github.com/salsa-rs/salsa.git"
rev = "05b4e3ebdcdc47730cdd359e7e97fb2470527279"
replace-with = "vendored-sources"
"""
        )


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    for shell in ["bash", "fish", "zsh"]:
        with open(self.cwd / f"ruff.{shell}", "w") as f:
            self.do(
                "./target/release/ruff",
                "--generate-shell-completion",
                shell,
                stdout=f,
            )


def do_check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def post_install(self):
    for shell in ["bash", "fish", "zsh"]:
        self.install_completion(f"ruff.{shell}", shell)
    self.install_license("LICENSE")
