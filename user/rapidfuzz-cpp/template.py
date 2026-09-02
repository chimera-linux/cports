pkgname = "rapidfuzz-cpp"
pkgver = "3.3.4"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DRAPIDFUZZ_BUILD_TESTING=ON"]
# experimental::MultiJaro (SIMD) misreturns 0.0 for identical strings
make_check_args = ["-E", "^Jaro$"]
hostmakedepends = ["cmake", "ninja"]
checkdepends = ["catch2-devel"]
pkgdesc = "Rapid fuzzy string matching in C++ using the Levenshtein distance"
license = "MIT"
url = "https://github.com/rapidfuzz/rapidfuzz-cpp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "a0dd2ef361cac165e12076696e7c7e8d069a2908abd9599ad4bd190de33f9881"

if self.profile().cross:
    # FetchContent(Catch2) fails: no network, no checkdepends in cross
    configure_args = ["-DRAPIDFUZZ_BUILD_TESTING=OFF"]


def post_install(self):
    self.install_license("LICENSE")
