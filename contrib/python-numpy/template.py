pkgname = "python-numpy"
pkgver = "2.0.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "pkgconf",
    "python-build",
    "python-cython",
    "python-meson",
    "python-installer",
]
makedepends = ["python-devel", "openblas-devel"]
depends = ["python"]
checkdepends = [
    "python-hypothesis",
    "python-pytest-xdist",
]
pkgdesc = "Package for scientific computing with Python"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://numpy.org"
source = f"https://github.com/numpy/numpy/releases/download/v{pkgver}/numpy-{pkgver}.tar.gz"
sha256 = "cf5d1c9e6837f8af9f92b6bd3e86d513cdc11f60fd62185cc49ec7d1aba34864"
hardening = ["!int"]


# this is identical to the default do_check, we just have to change cwd
def do_check(self):
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
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
        "-k",
        "not test_cython"
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
    self.rm(
        self.destdir
        / f"usr/lib/python{self.python_version}/site-packages/numpy/*/lib/lib*.a",
        glob=True,
    )


@subpackage("python-numpy-tests")
def _tests(self):
    self.pkgdesc = f"{pkgdesc} (tests)"
    self.depends += ["python"]
    return [
        "usr/lib/python*/site-packages/numpy/*/tests/",
        "usr/lib/python*/site-packages/numpy/tests/",
    ]
