pkgname = "python-s3transfer"
pkgver = "0.10.1"
pkgrel = 0
build_style = "python_pep517"
make_check_args = [
    # needs credentials
    "--deselect=tests/integration",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-botocore"]
checkdepends = depends + ["python-pytest-xdist"]
pkgdesc = "Amazon S3 transfer manager for python"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/s3transfer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b6d42d2c81791486166a7b5fc4b4159e7b7ca6c6242d01310eebf546e16382eb"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
