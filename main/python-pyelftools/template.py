pkgname = "python-pyelftools"
pkgver = "0.31"
pkgrel = 0
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
sha256 = "c774416b10310156879443b81187d182d8d9ee499660380e645918b50bc88f99"


def check(self):
    # we simply can't run the dwarfdump and readelf tests; they depend on a
    # dwarfdump and readelf built targeting glibc and x86_64. we could
    # force the tests to use our own stuff, but that kinda defeats the
    # point with upstream's intention of having a predictable base
    for test in ["run_all_unittests.py", "run_examples_test.py"]:
        self.do("python", f"test/{test}")
