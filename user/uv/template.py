pkgname = "uv"
pkgver = "0.7.3"
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
license = "Apache-2.0 OR MIT"
url = "https://github.com/astral-sh/uv"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ad6dbd387c8627571580c81e9e127555d4b91d2bec4578876c5f2505a4cda29c"
# too many of them need net
# completions with host bin
options = ["!check", "!cross"]

if self.profile().wordsize == 32:
    broken = "needs atomic64"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_build(self):
    for cmd in ["uv", "uvx"]:
        for shell in ["bash", "fish", "nushell", "zsh"]:
            with open(self.cwd / f"{cmd}.{shell}", "w") as cf:
                self.do(
                    f"./target/{self.profile().triplet}/release/{cmd}",
                    "--generate-shell-completion",
                    shell,
                    stdout=cf,
                )


def check(self):
    from cbuild.util import cargo

    cargo.Cargo(self).check()


def post_install(self):
    self.install_license("LICENSE-MIT")
    for cmd in ["uv", "uvx"]:
        for shell in ["bash", "fish", "nushell", "zsh"]:
            self.install_completion(f"{cmd}.{shell}", shell, cmd)
