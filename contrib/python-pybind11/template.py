pkgname = "python-pybind11"
pkgver = "2.11.1"
pkgrel = 0
build_style = "python_pep517"
make_build_args = ["--skip-dependency-check"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
makedepends = [
    "boost-devel",
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
checkdepends = ["python-pytest"]
pkgdesc = "Seamless operability between C++11 and Python"
maintainer = "Duncan Bellamy <dunk@denkimushi.com>"
license = "BSD-3-Clause"
url = "https://pybind11.readthedocs.io/en/stable/index.html"
source = f"https://github.com/pybind/pybind11/archive/refs/tags/v{pkgver}.zip"
sha256 = "b011a730c8845bfc265f0f81ee4e5e9e1d354df390836d2a25880e123d021f89"


def pre_check(self):
    from cbuild.util import cmake

    cmake.configure(
        self,
        build_dir="build-tests",
    )
    cmake.build(self, "build-tests")


def do_check(self):
    # deselected test has RuntimeError
    self.do(
        "sh",
        "-c",
        "cd build-tests/tests && python3 -m \
        pytest --deselect test_exceptions.py::test_cross_module_exception_translator",
    )


def post_install(self):
    self.install_license("LICENSE")

    self.install_dir("usr/include")
    self.install_dir("usr/share/cmake")
    self.install_dir("usr/share/pkgconfig")
    _pypath = f"lib/python{self.python_version}/site-packages/pybind11"
    self.install_link(
        f"../{_pypath}/include/pybind11",
        "usr/include/pybind11",
    )
    self.install_link(
        f"../../{_pypath}/share/cmake/pybind11",
        "usr/share/cmake/pybind11",
    )
    self.install_link(
        f"../../{_pypath}/share/pkgconfig/pybind11.pc",
        "usr/share/pkgconfig/pybind11.pc",
    )


@subpackage("python-pybind11-devel")
def _devel(self):
    return self.default_devel()
