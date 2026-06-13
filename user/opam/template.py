pkgname = "opam"
pkgver = "2.5.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-vendored-deps",
    "--with-mccs",
]
make_dir = "."
make_build_target = "all"
make_check_target = "tests"
hostmakedepends = ["automake"]
makedepends = ["ocaml-compiler-libs"]
depends = ["bash", "bubblewrap", "curl", "libarchive-progs", "unzip"]
pkgdesc = "OCaml package manager"
license = "LGPL-2.1-only WITH OCaml-LGPL-linking-exception"
url = "https://opam.ocaml.org"
source = f"https://github.com/ocaml/opam/releases/download/{pkgver}/opam-full-{pkgver}.tar.gz"
sha256 = "48c5bfaf5f5c4048cc5f40025de7385f5bad3a8269756216cd6dd2f2150033ed"
# check requires bubblewrap and fails within containers
options = ["!check", "!cross", "!parallel"]
