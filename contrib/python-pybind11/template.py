pkgname = "python-pybind11"
pkgver = "2.12.0"
pkgrel = 0
build_style = "python_pep517"
make_build_args = ["--skip-dependency-check"]
make_check_args = [
    # finds wrong cflags in sample project
    "--deselect=tests/extra_setuptools/test_setuphelper.py::test_simple_setup_py",
    # fail
    "--deselect=tests/test_exceptions.py::test_cross_module_exception_translator",
    "--ignore=tests/extra_python_package/test_files.py",
    # missing trampoline_module/widget_module
    "--ignore=tests/test_embed/test_interpreter.py",
    "--ignore=tests/test_embed/test_trampoline.py",
]
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
source = (
    f"https://github.com/pybind/pybind11/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "bf8f242abd1abcd375d516a7067490fb71abd79519a282d22b6e4d19282185a7"


def pre_check(self):
    from cbuild.util import cmake

    cmake.configure(
        self,
        build_dir="build-tests",
    )
    cmake.build(self, "build-tests")


def post_install(self):
    self.install_license("LICENSE")

    self.install_dir("usr/include")
    self.install_dir("usr/share/cmake")
    self.install_dir("usr/share/pkgconfig")
    _pypath = f"lib/python{self.python_version}/site-packages/pybind11"
    self.install_link(
        "usr/include/pybind11",
        f"../{_pypath}/include/pybind11",
    )
    self.install_link(
        "usr/share/cmake/pybind11",
        f"../../{_pypath}/share/cmake/pybind11",
    )
    self.install_link(
        "usr/share/pkgconfig/pybind11.pc",
        f"../../{_pypath}/share/pkgconfig/pybind11.pc",
    )


@subpackage("python-pybind11-devel")
def _devel(self):
    return self.default_devel()
