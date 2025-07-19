pkgname = "ocaml"
pkgver = "5.3.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libdir=/usr/lib/ocaml",
    "--disable-installing-source-artifacts",
    "--enable-ocamltest",
]
configure_gen = []
make_dir = "."
make_check_target = "tests"
makedepends = ["zstd-devel"]
depends = [*makedepends]
pkgdesc = "Main implementation of the OCaml programming language"
license = "LGPL-2.1-only"
url = "https://ocaml.org"
source = f"https://github.com/ocaml/ocaml/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb9eab2f21758d3cfb1e78c7f83f0b4dd6302824316aba4abee047a5a4f85029"
tools = {"ASPP": "cc -c", "AS": "cc -c"}
# disable usban integer checks due to camlInternalFormatBasics module failing to build
hardening = ["!int"]
options = ["!cross"]


@subpackage("ocaml-static")
def _(self):
    return ["usr/lib/ocaml/*.a", "usr/lib/ocaml/*/*.a"]
