pkgname = "gas"
pkgver = "2.41"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-gold",
    "--disable-gprof",
    "--disable-gprofng",
    "--disable-ld",
    "--disable-multilib",
    "--disable-nls",
    "--disable-shared",
    "--disable-werror",
    "--with-system-zlib",
    "--with-zstd",
]
# require a very specific autotools
configure_gen = []
make_cmd = "gmake"
hostmakedepends = [
    "gmake",
    "pkgconf",
    "texinfo",
]
makedepends = [
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "GNU Assembler"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://www.gnu.org/software/binutils"
source = f"https://ftp.gnu.org/gnu/binutils/binutils-{pkgver}.tar.xz"
sha256 = "ae9a5789e23459e59606e6714723f2d3ffc31c03174191ef0d015bdf06007450"
hardening = ["vis", "cfi"]
# todo
options = ["!cross"]


def do_install(self):
    self.install_bin(self.cwd / self.make_dir / "gas/as-new", name="gas")
    self.install_man(self.cwd / self.make_dir / "gas/doc/as.1")
    # also make it as(1) since nothing else provides it
    self.install_link("gas", "usr/bin/as")
