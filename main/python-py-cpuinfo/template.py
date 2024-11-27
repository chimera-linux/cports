pkgname = "python-py-cpuinfo"
pkgver = "9.0.0"
pkgrel = 1
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python"]
checkdepends = ["python-pytest-xdist"]
pkgdesc = "Python module for getting CPU info"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "MIT"
url = "https://github.com/workhorsy/py-cpuinfo"
source = f"$(PYPI_SITE)/p/py-cpuinfo/py-cpuinfo-{pkgver}.tar.gz"
sha256 = "3cdbbf3fac90dc6f118bfd64384f309edeadd902d7c8fb17f02ffa1fc3f49690"


def init_check(self):
    self.make_check_args += [
        f"--numprocesses={self.make_jobs}",
        "--dist=worksteal",
    ]


def post_install(self):
    self.install_license("LICENSE")
