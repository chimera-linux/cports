pkgname = "python-nanobind"
pkgver = "2.7.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "ninja",
    "python-build",
    "python-installer",
    "python-scikit_build_core",
]
depends = ["python"]
checkdepends = ["cmake", "python-devel", "python-pytest", "python-tests"]
pkgdesc = "C++/Python bindings generator"
license = "BSD-3-Clause"
url = "https://github.com/wjakob/nanobind"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    "https://github.com/Tessil/robin-map/archive/v1.4.0.tar.gz",
]
source_paths = [".", "ext/robin_map"]
sha256 = [
    "6c8c6bf0435b9d8da9312801686affcf34b6dbba142db60feec8d8e220830499",
    "7930dbf9634acfc02686d87f615c0f4f33135948130b8922331c16d90a03250c",
]


def check(self):
    self.do(
        "cmake",
        "-S",
        ".",
        "-B",
        ".test-build",
        "-DNB_TEST_STABLE_ABI=ON",
        "-DNB_TEST_SHARED_BUILD=1",
    )
    self.do("cmake", "--build", ".test-build", f"-j{self.make_jobs}")
    self.do("python", "-m", "pytest", wrksrc=".test-build")


def post_install(self):
    self.install_license("LICENSE")
    for f in ["cmake", "ext", "include", "src"]:
        self.rename(
            f"usr/lib/python*/site-packages/nanobind/{f}",
            f"usr/share/nanobind/{f}",
            relative=False,
            glob=True,
        )


@subpackage("python-nanobind-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel(extra=["usr/share/nanobind"])
