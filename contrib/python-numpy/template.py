pkgname = "python-numpy"
pkgver = "1.26.4"
pkgrel = 2
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
checkdepends = ["meson", "python-hypothesis", "python-pytest"]
pkgdesc = "Package for scientific computing with Python"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "BSD-3-Clause"
url = "https://numpy.org"
source = f"https://github.com/numpy/numpy/releases/download/v{pkgver}/numpy-{pkgver}.tar.gz"
sha256 = "2a02aba9ed12e4ac4eb3ea9421c420301a0c6460d9830d74a9df87efa4912010"
hardening = ["!int"]


# numpy includes a test suite
# create a venv manually and run it
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
        "-c",
        "import numpy; numpy.test()",
        # can't run from source directory
        wrksrc="/tmp",
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
