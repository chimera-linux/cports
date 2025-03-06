pkgname = "python-pyelftools"
pkgver = "0.32"
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
license = "Unlicense"
url = "https://github.com/eliben/pyelftools"
source = f"$(PYPI_SITE)/p/pyelftools/pyelftools-{pkgver}.tar.gz"
sha256 = "6de90ee7b8263e740c8715a925382d4099b354f29ac48ea40d840cf7aa14ace5"


def check(self):
    # we simply can't run the dwarfdump and readelf tests; they depend on a
    # dwarfdump and readelf built targeting glibc and x86_64. we could
    # force the tests to use our own stuff, but that kinda defeats the
    # point with upstream's intention of having a predictable base
    for test in ["run_all_unittests.py", "run_examples_test.py"]:
        self.do("python", f"test/{test}")
