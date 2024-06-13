pkgname = "racket"
pkgver = "8.13"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_wrksrc = "src"
build_style = "gnu_configure"
configure_args = ["--disable-strip"]
configure_gen = []
hostmakedepends = ["automake", "sqlite"]
makedepends = [
    "libffi-devel",
    "lz4-devel",
    "ncurses-devel",
    "zlib-devel",
]
pkgdesc = "Language-oriented programming language"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "MIT OR Apache-2.0"
url = "https://racket-lang.org"
source = f"https://download.racket-lang.org/installers/{pkgver}/racket-{pkgver}-src-builtpkgs.tgz"
sha256 = "e24008a428a4a62019c5f27763404e99ed103f02d9a71336145bd62626aa2f1f"
# no tests, cross requires external chezscheme
options = ["!check", "!cross"]

match self.profile().arch:
    case "aarch64" | "x86_64":
        configure_args += ["--enable-csonly", "--enable-csdefault"]
    case "ppc64le" | "riscv64":
        configure_args += ["--enable-bconly", "--enable-bcdefault"]
        makedepends += ["libucontext-devel"]
        tool_flags = {
            "CFLAGS": ["-D_GNU_SOURCE"],
            "LDFLAGS": ["-lucontext"],
        }


def post_extract(self):
    self.rm("src/bc/foreign/libffi", recursive=True)


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("racket-devel")
def _devel(self):
    return self.default_devel()
