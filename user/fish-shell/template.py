pkgname = "fish-shell"
pkgver = "4.1.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_BUILD_TYPE=Release"]
make_check_target = "fish_run_tests"
hostmakedepends = ["cargo-auditable", "cmake", "gettext", "ninja", "pkgconf"]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["procps", "python", "python-pexpect"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "52873934fc1ee21a1496e9f4521409013e540f77cbf29142a1b17ab93ffaafac"


def prepare(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


def post_install(self):
    for fishbin in ["fish_indent", "fish_key_reader"]:
        self.uninstall(f"usr/bin/{fishbin}")
        self.install_link(f"usr/bin/{fishbin}", "fish")
    self.install_shell("/usr/bin/fish")
