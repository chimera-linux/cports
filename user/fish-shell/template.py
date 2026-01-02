pkgname = "fish-shell"
pkgver = "4.4.0"
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
checkdepends = ["procps", "python"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "529e1072c034f6c9d21a922c359886df75129c3d81a15bd8656a3c4860993ad5"
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
