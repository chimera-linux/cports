pkgname = "ruff"
pkgver = "0.4.8"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo",
    "python-build",
    "python-installer",
    "python-maturin",
]
makedepends = ["rust-std"]
pkgdesc = "Python formatter and linter"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "https://docs.astral.sh/ruff"
source = f"https://github.com/astral-sh/ruff/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "983d61b9602b800e9118e9e52eeca4f8f2c3697e7d281e230619b39fa21e4c9b"
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
