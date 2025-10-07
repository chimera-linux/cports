pkgname = "python-numpy"
pkgver = "2.3.2"
pkgrel = 1
build_style = "python_pep517"
make_build_args = []
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-installer",
    "python-meson",
]
makedepends = ["python-devel", "openblas-devel"]
depends = ["python"]
checkdepends = [
    "python-hypothesis",
    "python-pytest-xdist",
]
pkgdesc = "Package for scientific computing with Python"
license = "BSD-3-Clause"
url = "https://numpy.org"
source = f"https://github.com/numpy/numpy/releases/download/v{pkgver}/numpy-{pkgver}.tar.gz"
sha256 = "e0486a11ec30cdecb53f184d496d1c6a20786c81e55e41640270130056f8ee48"
hardening = ["!int"]
# exec format error
options = ["!cross"]

if self.profile().arch in ["aarch64", "loongarch64", "riscv64"]:
    # FIXME: segfault in python in
    # test_half_ordering and test_sort_degrade
    # with this enabled
    # also fails to build on loongarch
    make_build_args += [
        "--config-setting",
        "setup-args=-Ddisable-highway=true",
    ]


# this is identical to the default check, we just have to change cwd
def check(self):
    whl = list(
        map(
            lambda p: str(p.relative_to(self.cwd)),
            self.cwd.glob("dist/*.whl"),
        )
    )

    self.rm(".cbuild-checkenv", recursive=True, force=True)
    self.do(
        "python3",
        "-m",
        "venv",
        "--without-pip",
        "--system-site-packages",
        "--clear",
        ".cbuild-checkenv",
    )

    envpy = self.chroot_cwd / ".cbuild-checkenv/bin/python3"

    self.do(envpy, "-m", "installer", *whl)
    self.do(
        envpy,
        "-m",
        "pytest",
        "--pyargs",
        "numpy",
        "-m",
        "not slow",
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        # fails casts/float stuff on aarch64
        f"--ignore=../.cbuild-checkenv/lib/python{self.python_version}/site-packages/numpy/_core/tests/test_casting_floatingpoint_errors.py",
        f"--ignore=../.cbuild-checkenv/lib/python{self.python_version}/site-packages/numpy/_core/tests/test_umath.py",
        f"--ignore=../.cbuild-checkenv/lib/python{self.python_version}/site-packages/numpy/linalg/tests/test_linalg.py",
        f"--ignore=../.cbuild-checkenv/lib/python{self.python_version}/site-packages/numpy/_core/tests/test_numeric.py",
        "-k",
        "not test_cython"
        # more float aarch64 stuff
        + " and not test_vecdot_complex"
        + " and not test_dot_errstate[longdouble]"
        # f2py stuff
        + " and not test_limited_api"
        + " and not test_no_py312_distutils_fcompiler"
        + " and not test_untitled_cli"
        + " and not test_features"
        # ppc
        + " and not test_ppc64_ibm_double_double128",
        # can't run from source directory
        wrksrc=f"{self.chroot_cwd}/tools",
        path=[envpy.parent],
    )


def post_install(self):
    self.install_license("LICENSE.txt")
    # remove static libs
    self.uninstall(
        f"usr/lib/python{self.python_version}/site-packages/numpy/*/lib/lib*.a",
        glob=True,
    )


@subpackage("python-numpy-tests")
def _(self):
    self.subdesc = "tests"
    self.depends = [
        *checkdepends,
        self.parent,
    ]
    return [
        "usr/lib/python*/site-packages/numpy/*/tests/",
        "usr/lib/python*/site-packages/numpy/tests/",
    ]
