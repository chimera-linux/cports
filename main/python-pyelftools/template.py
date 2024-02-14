pkgname = "python-pyelftools"
pkgver = "0.30"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
pkgdesc = "ELF and DWARF parsing library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Unlicense"
url = "https://github.com/eliben/pyelftools"
source = f"$(PYPI_SITE)/p/pyelftools/pyelftools-{pkgver}.tar.gz"
sha256 = "2fc92b0d534f8b081f58c7c370967379123d8e00984deb53c209364efd575b40"


def do_check(self):
    # we simply can't run the dwarfdump and readelf tests; they depend on a
    # dwarfdump and readelf built targeting glibc and x86_64. we could
    # force the tests to use our own stuff, but that kinda defeats the
    # point with upstream's intention of having a predictable base
    for test in ["run_all_unittests.py", "run_examples_test.py"]:
        self.do("python", f"test/{test}")
