pkgname = "fish-shell"
pkgver = "4.0.8"
pkgrel = 0
build_style = "cmake"
make_check_target = "fish_run_tests"
hostmakedepends = ["cargo-auditable", "cmake", "ninja", "pkgconf", "gettext"]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["python", "procps"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "7f779d13aa55d2fa3afc17364c61ab9edc16faa1eac5851badeffb4e73692240"
# FIXME lintpixmaps
options = ["!lintpixmaps"]


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    self.install_shell("/usr/bin/fish")
