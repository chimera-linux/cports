pkgname = "libchewing"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cmake"
# The test fails when run in parallel.
make_check_args = ["-j1"]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "corrosion",
    "ninja",
    "pkgconf",
]
makedepends = ["sqlite-devel", "ncurses-devel", "rust-std"]
pkgdesc = "Intelligent phonetic input method library"
license = "LGPL-2.1-or-later"
url = "https://chewing.im"
source = f"https://github.com/chewing/libchewing/releases/download/v{pkgver}/libchewing-{pkgver}.tar.zst"
sha256 = "4f2538affadd0c09738166d8a700853866811c4094fc256c05585f443e50b842"
tool_flags = {"CFLAGS": ["-DHAVE_NCURSES_H"]}


def post_patch(self):
    from cbuild.util import cargo

    cargo.Cargo(self, wrksrc=".").vendor()


def init_build(self):
    from cbuild.util import cargo

    renv = cargo.get_environment(self)
    self.make_env.update(renv)


@subpackage("libchewing-devel")
def _(self):
    return self.default_devel()
