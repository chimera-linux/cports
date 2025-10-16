pkgname = "opam"
pkgver = "2.4.1"
pkgrel = 0
build_style = "makefile"
make_build_target = "cold"
make_install_target = "install"
make_install_args = ["prefix=/usr"]
makedepends = ["curl", "rsync", "unzip", "bubblewrap", "bash", "clang", "gmake"]
depends = [*makedepends]
pkgdesc = "OCaml Package Manager"
license = "LGPL-2.1-only WITH OCaml-LGPL-linking-exception"
url = "https://opam.ocaml.org"
source = f"https://github.com/ocaml/opam/releases/download/{pkgver}/opam-full-{pkgver}.tar.gz"
sha256 = "c4d053029793c714e4e7340b1157428c0f90783585fb17f35158247a640467d9"
tools = {"ASPP": "cc -c", "AS": "cc -c"}
hardening = ["!int"]
# check is disabled because it requires bubblewrap and doesn't work inside the sandbox
options = ["!cross", "!check"]
