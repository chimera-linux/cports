pkgname = "ruff"
pkgver = "0.4.1"
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
sha256 = "7213ad13b15e766fb4f5d2fa24ffe1a1a55b47822a159e3c8f64b4a0e6ebca49"
# generates completions with host bin
options = ["!cross"]


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()
    cargo.setup_vendor(self)


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
