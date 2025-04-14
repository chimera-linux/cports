pkgname = "racket"
pkgver = "8.16"
pkgrel = 0
archs = ["aarch64", "ppc64le", "riscv64", "x86_64"]
build_wrksrc = "src"
build_style = "gnu_configure"
configure_args = ["--disable-strip"]
configure_gen = []
hostmakedepends = ["automake", "sqlite"]
makedepends = [
    "libffi8-devel",
    "lz4-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Language-oriented programming language"
license = "MIT OR Apache-2.0"
url = "https://racket-lang.org"
source = f"https://download.racket-lang.org/installers/{pkgver}/racket-{pkgver}-src-builtpkgs.tgz"
sha256 = "44d7c1ab34b52588f90dc22b15d96110e104d0c88ed1869f85b6f03c99843078"
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
def _(self):
    return self.default_devel()
