pkgname = "python-rapidfuzz"
pkgver = "3.14.6"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"RAPIDFUZZ_BUILD_EXTENSION": "1"}
hostmakedepends = [
    "ninja",
    "python-build",
    "python-installer",
    "python-scikit_build_core",
]
makedepends = ["python-devel", "rapidfuzz-cpp", "taskflow"]
depends = ["python"]
checkdepends = ["python-hypothesis", "python-pytest"]
pkgdesc = "Rapid fuzzy string matching in Python using various string metrics"
license = "MIT"
url = "https://github.com/rapidfuzz/RapidFuzz"
source = f"$(PYPI_SITE)/r/rapidfuzz/rapidfuzz-{pkgver}.tar.gz"
sha256 = "e13a8160d017b499ec7a2fa9d0ce1ae2e7377080815785819f966fb235d4eb60"
# python_pep517 doesn't pass a CMake toolchain to scikit-build-core
options = ["!cross"]


def post_install(self):
    self.install_license("LICENSE")
