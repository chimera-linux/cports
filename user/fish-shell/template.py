pkgname = "fish-shell"
pkgver = "4.8.1"
pkgrel = 0
build_style = "cmake"
make_check_target = "fish_run_tests"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
    "python-sphinx",
]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["procps", "python-pexpect"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "0eb86a851e865e934a7c2091a73d7695225e78f0e00a7bb96d5f877d76c65782"
# uses a compiled binary to build docs
options = ["!cross"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_shell("/usr/bin/fish")
    for fishbin in ["fish_indent", "fish_key_reader"]:
        self.uninstall(f"usr/bin/{fishbin}")
        self.install_link(f"usr/bin/{fishbin}", "fish")
    self.uninstall("etc/fish")
