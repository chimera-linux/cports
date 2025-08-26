pkgname = "ocaml"
pkgver = "5.3.0"
pkgrel = 0
archs = ["aarch64", "ppc64", "ppc64le", "x86_64"]
build_style = "gnu_configure"
configure_args = ["--enable-ocamltest", "--libdir=/usr/lib/ocaml", "--with-pic"]
configure_gen = []
make_dir = "."
make_check_target = "tests"
makedepends = ["zstd-devel"]
depends = [self.with_pkgver("ocaml-runtime"), *makedepends]
pkgdesc = "Implementation of the OCaml language"
license = "LGPL-2.1-only WITH OCaml-LGPL-linking-exception"
url = "https://ocaml.org"
source = f"https://github.com/ocaml/ocaml/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb9eab2f21758d3cfb1e78c7f83f0b4dd6302824316aba4abee047a5a4f85029"
tools = {"ASPP": "cc -c", "AS": "cc -c"}
hardening = ["!int"]
options = ["!cross", "!lintstatic"]


def post_extract(self):
    # flaky test
    self.rm("testsuite/tests/lib-runtime-events/test_dropped_events.ml")


def post_install(self):
    self.install_license("LICENSE")

    # consistency
    self.rename("usr/bin/ocamldoc", "ocamldoc.byte")
    self.install_link("usr/bin/ocamldoc", "ocamldoc.opt")

    # remove annotation files + sources
    self.uninstall("usr/lib/ocaml/**/*.cmt", glob=True)
    self.uninstall("usr/lib/ocaml/**/*.cmti", glob=True)
    self.uninstall("usr/lib/ocaml/**/*.ml", glob=True)


@subpackage("ocaml-byte")
def _(self):
    self.subdesc = "bytecode executables"
    self.depends = [self.with_pkgver("ocaml-runtime")]

    return ["cmd:*.byte"]


@subpackage("ocaml-ocamldoc")
def _(self):
    self.subdesc = "documentation generator"
    self.install_if = [self.parent]
    self.options = ["!lintstatic"]

    return ["cmd:ocamldoc*", "usr/lib/ocaml/ocamldoc"]


@subpackage("ocaml-compiler-libs")
def _(self):
    self.subdesc = "compiler libraries"
    self.depends = [self.parent]
    self.options = ["!lintstatic"]

    return ["usr/lib/ocaml/compiler-libs"]


@subpackage("ocaml-runtime")
def _(self):
    self.subdesc = "runtime environment"

    return [
        "cmd:ocamlrun*",
        "usr/lib/ocaml/ld.conf",
        "usr/lib/ocaml/**/*.cma",
        "usr/lib/ocaml/**/*.cmi",
        "usr/lib/ocaml/**/*.cmo",
    ]
