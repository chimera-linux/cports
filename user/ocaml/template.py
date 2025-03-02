pkgname = "ocaml"
pkgver = "5.3.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--libdir=/usr/lib/ocaml",
    "--bindir=/usr/bin",
    "--mandir=/usr/share/man",
    f"--docdir=/usr/share/doc/{pkgname}",
    "--disable-installing-source-artifacts",
]
make_check_target = "tests"
hostmakedepends = ["zstd-devel"]
depends = ["clang", "ocaml-static"]
pkgdesc = "Main implementation of the ocaml programming language"
maintainer = "chameko <chameko.c@gmail.com>"
license = "LGPL-2.1-only"
url = "https://ocaml.org"
source = f"https://github.com/ocaml/ocaml/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb9eab2f21758d3cfb1e78c7f83f0b4dd6302824316aba4abee047a5a4f85029"
tools = {"ASPP": "cc -c", "AS": "cc -c"}
# disable usban integer checks as breaks otherwise
hardening = ["!int"]
# disable tests
options = ["!check"]

# Have ocaml compile native binaries on architectures it supports
# and bytecode on others
match self.profile().arch:
    case "x86_64" | "aarch64" | "riscv64" | "s390x" | "ppc64le":
        configure_args += [
            "--enable-native-compiler",
            "--enable-native-toplevel",
            "--disable-installing-bytecode-programs",
        ]
        make_build_target = "world.opt"
        self.log(f"Building native compiler for {self.profile().arch}")
    case _:
        configure_args += [
            "--disable-native-compiler",
            "--disable-native-toplevel",
            "--enable-installing-bytecode-programs",
        ]
        make_build_target = "world"
        self.log(f"Building bytecode compiler for {self.profile().arch}")


def pre_check():
    from cbuild.util import make

    make.invoke(targets=["ocamltest"])


@subpackage("ocamldoc")
def _(self):
    self.subdesc = "Ocaml documentation generator"
    self.depends = [self.with_pkgver("ocamldoc-static")]
    return ["usr/bin/ocamldoc*"]


@subpackage("ocamldoc-static")
def _(self):
    return ["usr/lib/ocaml/ocamldoc"]


@subpackage("ocaml-compiler-libs-static")
def _(self):
    self.subdesc = "Modules used internally by the ocaml compiler"
    self.depends = [self.parent]
    return ["usr/lib/ocaml/compiler-libs/*.a"]


@subpackage("ocaml-compiler-libs")
def _(self):
    self.subdesc = "Modules used internally by the ocaml compiler"
    self.depends = [self.parent, self.with_pkgver("ocaml-compiler-libs-static")]
    return ["usr/lib/ocaml/compiler-libs"]

@subpackage("ocaml-static")
def _(self):
    return ["usr/lib/ocaml/*.a", "usr/lib/ocaml/*/*.a"]
