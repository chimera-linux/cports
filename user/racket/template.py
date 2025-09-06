pkgname = "racket"
pkgver = "8.18"
pkgrel = 0
build_wrksrc = "src"
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--disable-strip",
    "--enable-scheme=/usr/bin/scheme",
    "--enable-csonly",
    "--enable-csdefault",
]
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
sha256 = "59036cdc218ade49f1890349345f3cb470425d9edc0c677ea28690ce12d6cf2b"
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
        configure_args += [
            f"--enable-mach=tpb{self.profile().wordsize}{self.profile().endian[0]}",
        ]
        configure_args += ["--enable-pb"]


def post_extract(self):
    self.rm("src/bc/foreign/libffi", recursive=True)


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("racket-devel")
def _(self):
    return self.default_devel()
