pkgname = "ocaml"
pkgver = "5.3.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--disable-installing-source-artifacts",
    "--enable-mmap-map-stack",
    "--enable-ocamldebug",
    "--enable-ocamltest",
    "--mandir=/usr/share/man",
    "--prefix=/usr",
]
make_check_target = "tests"
hostmakedepends = ["file", "gmake"]
makedepends = ["zstd-devel"]
pkgdesc = "Industrial-strength functional programming language"
license = "LGPL-2.1-only WITH OCaml-LGPL-linking-exception"
url = "https://ocaml.org"
source = f"https://github.com/ocaml/ocaml/releases/download/{pkgver}/ocaml-{pkgver}.tar.gz"
sha256 = "22c1dd9de21bf43b62d1909041fb5fad648905227bf69550a6a6bef31e654f38"
options = ["!cross", "!lintstatic"]

## https://github.com/ocaml/ocaml/issues/5934
# runtime/interp.c:1180:12: runtime error: signed integer overflow: 9223372036854775807 + 2 cannot be represented in type 'value' (aka 'long')
# SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior runtime/interp.c:1180:12
# make[2]: *** [Makefile:118: camlinternalFormatBasics.cmi] Error 1
hardening = ["!int"]

if self.profile().arch in [
    "aarch64",
    "ppc64",
    "ppc64le",
    "riscv64",
    "s390x",
    "x86_64",
]:
    configure_args += [
        "--enable-native-compiler",
        "--enable-native-toplevel",
        "--disable-installing-bytecode-programs",
    ]
else:
    configure_args += [
        "--disable-native-compiler",
        "--disable-native-toplevel",
        "--enable-installing-bytecode-programs",
    ]


def post_extract(self):
    # https://github.com/ocaml/ocaml/issues/13757
    self.rm("testsuite/tests/lib-runtime-events/test_dropped_events.ml")
