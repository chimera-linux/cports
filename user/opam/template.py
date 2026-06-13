pkgname = "opam"
pkgver = "2.5.2"
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
# a bunch of these are needed for toolchain management
# we leave a compiler out as that's user choice
depends = [
    "bash",
    "bubblewrap",
    "curl",
    "gmake",
    "libarchive-progs",
    "rsync",
    "unzip",
]
checkdepends = [*depends]
pkgdesc = "OCaml package manager"
license = "LGPL-2.1-only WITH OCaml-LGPL-linking-exception"
url = "https://opam.ocaml.org"
source = f"https://github.com/ocaml/opam/releases/download/{pkgver}/opam-full-{pkgver}.tar.gz"
sha256 = "b3623809567f19ed6b5d679b8c7bbc0bdec9418bff4a875ff0799d446d8555c3"
# check requires bubblewrap and fails within containers
options = ["!check", "!cross", "!parallel"]


def post_install(self):
    # linking exception
    self.install_license("LICENSE")
