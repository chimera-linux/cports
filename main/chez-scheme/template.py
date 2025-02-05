pkgname = "chez-scheme"
pkgver = "10.1.0"
pkgrel = 0
build_style = "configure"
configure_args = ["--enable-libffi", "LZ4=-llz4", "ZLIB=-lz"]
make_check_target = "test-some-fast"
makedepends = [
    "libffi8-devel",
    "libx11-devel",
    "lz4-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Compiler and runtime system for R6RS Scheme"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://cisco.github.io/ChezScheme"
source = f"https://github.com/cisco/ChezScheme/releases/download/v{pkgver}/csv{pkgver}.tar.gz"
sha256 = "9181a6c8c4ab5e5d32d879ff159d335a50d4f8b388611ae22a263e932c35398b"
hardening = ["!int"]
# below
options = ["!cross"]

match self.profile().arch:
    case "aarch64":
        _machine = "tarm64le"
    case "armhf" | "armv7":
        _machine = "tarm32le"
    case "ppc":
        _machine = "tppc32le"
    case "riscv64":
        _machine = "trv64le"
    case "x86_64":
        _machine = "ta6le"
    case _:
        # portable bytecode
        _machine = f"tpb{self.profile().wordsize}{self.profile().endian[0]}"
        # also fails to link the tests
        options += ["!check"]

configure_args += [f"--machine={_machine}"]


def init_configure(self):
    self.configure_args += [
        f"--temproot={self.chroot_destdir}",
    ]
    self.env["ZUO_JOBS"] = str(self.make_jobs)


def post_install(self):
    # replace hard links with symlinks
    for dst, src in [
        ("scheme-script.boot", "scheme.boot"),
        ("scheme", "scheme-script"),
        ("petite", "scheme-script"),
    ]:
        self.uninstall(f"usr/lib/csv{pkgver}/{_machine}/{dst}")
        self.install_link(
            f"usr/lib/csv{pkgver}/{_machine}/{dst}",
            src,
        )

    # assume these files are unnecessary
    for filename in ["libkernel.a", "main.o", "scheme.h"]:
        self.uninstall(f"usr/lib/csv{pkgver}/{_machine}/{filename}")

    # let -doc pick up the examples
    self.install_dir("usr/share/doc/chez-scheme")
    self.rename(
        f"usr/lib/csv{pkgver}/examples",
        "usr/share/doc/chez-scheme/",
        relative=False,
    )
