pkgname = "python-ssh2"
pkgver = "1.1.2"
pkgrel = 1
build_style = "python_pep517"
make_build_env = {
    "SYSTEM_LIBSSH2": "1",
}
hostmakedepends = [
    "python-build",
    "python-cython",
    "python-installer",
    "python-setuptools",
]
makedepends = [
    "libssh2-devel",
    "python-devel",
]
checkdepends = [
    "openssh",
    "python-jinja2",
    "python-pytest",
    "python-pytest-rerunfailures",
]
pkgdesc = "Python bindings for libssh2"
license = "LGPL-2.1-only"
url = "https://github.com/ParallelSSH/ssh2-python"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "d911297f22322d39e85144900cccdb5b376492a92e17d1680611344451df4fbb"


# this is identical to the default check, we just have to change the pytest invocation
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
        # can't be -m pytest, otherwise it adds cwd to sys.path
        "/usr/bin/pytest",
        # use installed ssh2 module
        "--import-mode=importlib",
        path=[envpy.parent],
    )
