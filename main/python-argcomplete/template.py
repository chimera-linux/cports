pkgname = "python-argcomplete"
pkgver = "3.6.3"
pkgrel = 0
build_style = "python_pep517"
make_build_env = {"SETUPTOOLS_SCM_PRETEND_VERSION": pkgver}
hostmakedepends = [
    "python-build",
    "python-hatch_vcs",
    "python-hatchling",
    "python-installer",
]
depends = ["python"]
checkdepends = [
    "bash",
    "python-pexpect",
    "python-pip",
    "zsh",
]
pkgdesc = "Python tab completion plugin"
license = "Apache-2.0"
url = "https://github.com/kislyuk/argcomplete"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c733a0bae9e0382db134d3379095b6d1d7a76c48a9ee79e89ee784885f14b6d7"


# this is identical to the default check, but without pytest
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
    self.do(envpy, "test/test.py", path=[envpy.parent])
