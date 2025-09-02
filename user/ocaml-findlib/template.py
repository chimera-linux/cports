pkgname = "ocaml-findlib"
pkgver = "1.9.8"
pkgrel = 0
build_style = "configure"
configure_args = [
    "-bindir",
    "/usr/bin",
    "-mandir",
    "/usr/share/man",
    "-sitelib",
    "/usr/lib/ocaml",
    "-config",
    "/etc/findlib.conf",
]
make_build_args = ["all"]
hostmakedepends = ["ocaml"]
makedepends = ["ocaml-compiler-libs"]
pkgdesc = "OCaml library manager"
license = "MIT"
url = "https://projects.camlcity.org/projects/findlib.html"
source = f"https://download.camlcity.org/download/findlib-{pkgver}.tar.gz"
sha256 = "662c910f774e9fee3a19c4e057f380581ab2fc4ee52da4761304ac9c31b8869d"
options = ["etcfiles", "!cross", "!lintstatic"]

match self.profile().arch:
    # native archs
    case "aarch64" | "ppc64" | "ppc64le" | "riscv64" | "x86_64":
        make_build_args += ["opt"]


def check(self):
    # These are the libraries itest has tests for which also have META files in
    # the ocaml package.
    for i in ["str", "unix"]:
        self.do("./itest", i, env={"OCAMLFIND_CONF": "./findlib.conf"})


def post_install(self):
    self.install_license("LICENSE")
