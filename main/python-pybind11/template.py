pkgname = "python-pybind11"
pkgver = "3.0.4"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # finds wrong cflags in sample project
    "--deselect=tests/extra_setuptools/test_setuphelper.py::test_simple_setup_py",
    # fail
    "--deselect=tests/test_exceptions.py::test_cross_module_exception_translator",
    "--ignore=tests/extra_python_package/test_files.py",
    # missing trampoline_module/widget_module
    "--ignore=tests/test_with_catch/test_interpreter.py",
    "--ignore=tests/test_with_catch/test_trampoline.py",
    # hangs
    "--ignore=tests/test_multiple_interpreters.py",
    # contructor called twice
    "--deselect=tests/test_sequences_and_iterators.py::test_sequence",
    # can't find modules
    "--ignore=tests/test_standalone_enum_module.py",
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
    "python-scikit_build_core",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["eigen", "python-pytest-xdist"]
pkgdesc = "Seamless operability between C++11 and Python"
license = "BSD-3-Clause"
url = "https://pybind11.readthedocs.io/en/stable/index.html"
source = (
    f"https://github.com/pybind/pybind11/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "74b6a2c2b4573a400cafb6ecbf60c98df300cd3d0041296b913d02b2cbbb2676"
tool_flags = {"CXXFLAGS": []}
# tests disabled conditionally
options = []

if self.profile().arch == "ppc":
    # tests fail to build
    options += ["!check"]
elif self.profile().arch == "ppc64":
    tool_flags["CXXFLAGS"] += ["-DEIGEN_DONT_VECTORIZE"]


def post_build(self):
    from cbuild.util import cmake

    if not self.options["check"]:
        return

    cmake.configure(
        self,
        build_dir="build-tests",
    )
    cmake.build(self, "build-tests")


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


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
def _(self):
    return self.default_devel()
