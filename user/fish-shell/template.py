pkgname = "fish-shell"
pkgver = "4.3.3"
pkgrel = 0
build_style = "cmake"
configure_args = []
make_check_target = "fish_run_tests"
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = ["pcre2-devel", "rust-std"]
checkdepends = ["procps", "python"]
pkgdesc = "Friendly interactive command line shell"
license = "GPL-2.0-only"
url = "https://fishshell.com"
source = f"https://github.com/fish-shell/fish-shell/releases/download/{pkgver}/fish-{pkgver}.tar.xz"
sha256 = "eba0e7d325c1d46046bb9d29434e7e0dabf7f584eb156845005d688e10b86e57"


if self.profile().cross:
    configure_args += [
        f"-DRust_CARGO_TARGET={self.profile().triplet}",
        "-DWITH_DOCS=off",
    ]
else:
    hostmakedepends += ["python-sphinx"]


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
