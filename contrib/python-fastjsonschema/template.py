pkgname = "python-fastjsonschema"
pkgver = "2.19.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # pytest-benchmark
    "--deselect=tests/benchmarks/test_benchmark.py",
    # hangs
    "--deselect=tests/test_examples.py",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Python json schema validator"
maintainer = "psykose <alice@ayaya.dev>"
license = "BSD-3-Clause"
url = "https://horejsek.github.io/python-fastjsonschema"
source = f"$(PYPI_SITE)/f/fastjsonschema/fastjsonschema-{pkgver}.tar.gz"
sha256 = "e3126a94bdc4623d3de4485f8d468a12f02a67921315ddc87836d6e456dc789d"


def post_install(self):
    self.install_license("LICENSE")
