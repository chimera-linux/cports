pkgname = "python-nanobind"
pkgver = "2.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "ninja",
    "python-build",
    "python-installer",
    "python-scikit_build_core",
]
depends = ["python"]
checkdepends = ["cmake", "python-devel", "python-pytest"]
pkgdesc = "C++/Python bindings generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://github.com/wjakob/nanobind"
source = [
    f"{url}/archive/v{pkgver}.tar.gz",
    "https://github.com/Tessil/robin-map/archive/v1.3.0.tar.gz",
]
source_paths = [".", "ext/robin_map"]
sha256 = [
    "bb35deaed7efac5029ed1e33880a415638352f757d49207a8e6013fefb6c49a7",
    "a8424ad3b0affd4c57ed26f0f3d8a29604f0e1f2ef2089f497f614b1c94c7236",
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
