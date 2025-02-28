pkgname = "fish-shell"
pkgver = "4.0.0"
pkgrel = 2
build_style = "cmake"
make_check_target = "fish_run_tests"
hostmakedepends = ["cargo-auditable", "cmake", "ninja", "pkgconf", "gettext"]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "2fda5bd970357064d8d4c896e08285ba59965ca2a8c4829ca8a82bf3b89c69f3"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_shell("/usr/bin/fish")
