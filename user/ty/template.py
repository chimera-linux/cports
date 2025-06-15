pkgname = "ty"
pkgver = "0.0.1.6"
_ver = "0.0.1-alpha.6"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "cargo-auditable",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-maturin",
    "git",
]
makedepends = [
    "rust-std",
    "zstd-devel",
]
pkgdesc = "Python type checker and language server"
license = "MIT"
url = "https://github.com/astral-sh/ty"
# can't be arsed for an early alpha where there's not even working tarballs
options = ["!check"]


def fetch(self):
    self.do("git", "init", ".")
    self.do("git", "remote", "add", "origin", f"{url}.git")
    self.do("git", "fetch", "--depth", "1", "origin", _ver)
    self.do("git", "checkout", "FETCH_HEAD")
    self.do(
        "git", "submodule", "update", "--init", "--recursive", "--depth", "1"
    )


def extract(self):
    # noop
    return


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self).vendor(wrksrc="ruff")

    self.mv("ruff/.cargo", ".")
    self.do(
        "sed",
        "-i",
        "",
        "-e",
        's#directory = "vendor"#directory = "ruff/vendor"#',
        ".cargo/config.toml",
    )


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_license("LICENSE")
