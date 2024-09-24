pkgname = "uv"
pkgver = "0.4.16"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "Apache-2.0 OR MIT"
url = "https://github.com/astral-sh/uv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "28c40f5456afa30fac98bb0f3fe38740d8c3bda9425c75b21044efe30c9c3278"
# too many of them need net
# completions with host bin
options = ["!check", "!cross"]


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
