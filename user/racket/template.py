pkgname = "racket"
pkgver = "8.17"
pkgrel = 1
build_wrksrc = "src"
build_style = "gnu_configure"
configure_args = [
    "--disable-strip",
    "--enable-scheme=/usr/bin/scheme",
    "--enable-csonly",
    "--enable-csdefault",
]
configure_gen = []
hostmakedepends = [
    "automake",
    "chez-scheme",
    "sqlite",
]
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
sha256 = "bb98bd8b6d9eba56bd5107fe29be50ad8cd4fb7bb32fbd762c5bd259c15e706f"
# no tests, cross requires chezscheme version to match exactly
options = ["!check", "!cross"]

# same as main/chez-scheme
match self.profile().arch:
    case "aarch64":
        configure_args += ["--enable-mach=tarm64le"]
    case "armhf" | "armv7":
        configure_args += ["--enable-mach=tarm32le"]
    case "loongarch64":
        configure_args += ["--enable-mach=tla64le"]
    case "ppc":
        configure_args += ["--enable-mach=tppc32le"]
    case "riscv64":
        configure_args += ["--enable-mach=trv64le"]
    case "x86_64":
        configure_args += ["--enable-mach=ta6le"]
    case _:
        # portable bytecode
        configure_args += ["--enable-pb"]


def post_extract(self):
    self.rm("src/bc/foreign/libffi", recursive=True)


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("racket-devel")
def _(self):
    return self.default_devel()
