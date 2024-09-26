pkgname = "libchewing"
pkgver = "0.9.0"
pkgrel = 0
build_style = "cmake"
# The test fails when run in parallel.
make_check_args = ["-j1"]
hostmakedepends = [
    "cargo",
    "cmake",
    "corrosion",
    "ninja",
    "pkgconf",
]
makedepends = ["sqlite-devel", "ncurses-devel", "rust-std"]
pkgdesc = "Intelligent phonetic input method library"
maintainer = "xunil-cloud <river_electron@proton.me>"
license = "LGPL-2.1-or-later"
url = "https://chewing.im"
source = f"https://github.com/chewing/libchewing/releases/download/v{pkgver}/libchewing-{pkgver}.tar.zst"
sha256 = "58e62cd0649ba3856ffa7c67560c1cfbcbb8713342a533f7700587b51efe84e3"
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
