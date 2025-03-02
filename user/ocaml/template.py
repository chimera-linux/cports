pkgname = "ocaml"
pkgver = "5.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_script = "configure"
configure_args = [
    "--libdir=/usr/lib/ocaml/",
    "--disable-installing-source-artifacts",
    "--enable-ocamltest"
]
configure_gen = []
make_dir = "."
make_check_target = "tests"
makedepends = ["zstd-devel"]
depends = ["zstd-devel"]
pkgdesc = "Main implementation of the OCaml programming language"
license = "LGPL-2.1-only"
url = "https://ocaml.org"
source = f"https://github.com/ocaml/ocaml/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb9eab2f21758d3cfb1e78c7f83f0b4dd6302824316aba4abee047a5a4f85029"
tools = {"ASPP": "cc -c", "AS": "cc -c"}
# disable usban integer checks due to camlInternalFormatBasics module failing to build
hardening = ["!int"]

# Have ocaml compile native binaries on architectures it supports
# and bytecode on others
match self.profile().arch:
    case "x86_64" | "aarch64" | "riscv64" | "ppc64le":
        configure_args += [
            "--enable-native-compiler",
            "--enable-native-toplevel",
            "--disable-installing-bytecode-programs",
        ]
        make_build_target = "world"
    case "ppc":
        configure_args += [
            "--disable-native-compiler",
            "--disable-native-toplevel",
            "--enable-installing-bytecode-programs",
        ]
        make_build_target = "world.opt"
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"


def pre_check(self):
    from cbuild.util import make

    self.make.invoke()
    self.make.invoke(targets=["ocamltest"])


@subpackage("ocamldoc")
def _(self):
    self.subdesc = "Ocaml documentation generator"
    return ["usr/bin/ocamldoc*"]

@subpackage("ocaml-static")
def _(self):
    return ["usr/lib/ocaml/*.a"]
