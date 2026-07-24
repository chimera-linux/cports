pkgname = "open-adventure"
pkgver = "1.21"
pkgrel = 0
build_style = "makefile"
make_build_target = "advent"
make_build_args = [f"VERSION={pkgver}"]
make_build_env = {"CCFLAGS": "-U_FORTIFY_SOURCE"}
make_install_args = [f"VERSION={pkgver}"]
make_check_args = [f"VERSION={pkgver}"]
make_check_env = {"CCFLAGS": "-U_FORTIFY_SOURCE"}
makedepends = [
    "asciidoctor",
    "libedit-devel",
    "pkgconf",
    "python",
    "python-pyyaml",
]
# checkdepends = ["cppcheck", "pylint", "spellcheck"]
pkgdesc = "Colossal Cave Adventure, the 1995 430-point version"
license = "BSD-2-Clause"
url = "http://www.catb.org/~esr/open-adventure"
source = f"{url}/advent-{pkgver}.tar.gz"
sha256 = "80bc3d3dddd8fb1b8d9623663cdf88d58c9086e2e08e3000542eff66e48bdb80"
# TODO: add pylint package and reenable thiis
options = ["!check"]


def prepare(self):
    # for some reason the tarball has the tpl files in the root directory
    # ource code has it in a 'templates' directory
    self.mkdir("templates")
    self.mv("*.tpl", "templates", glob=True)


def install(self):
    self.install_bin("advent")
    self.install_license(self.files_path / "COPYING", name="LICENSE")
