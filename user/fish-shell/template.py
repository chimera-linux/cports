pkgname = "fish-shell"
pkgver = "4.2.1"
pkgrel = 0
build_style = "cmake"
make_check_target = "fish_run_tests"
hostmakedepends = ["cargo-auditable", "cmake", "gettext", "pkgconf", "ninja"]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["procps", "python"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "0f99222a3063377c91fbf78d9850edab7a0b91bdbed201cf79da48ea3a41f393"


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
