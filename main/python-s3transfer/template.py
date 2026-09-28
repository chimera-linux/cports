pkgname = "python-s3transfer"
pkgver = "0.17.1"
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
checkdepends = ["python-pytest-xdist", *depends]
pkgdesc = "Amazon S3 transfer manager for python"
license = "Apache-2.0"
url = "https://github.com/boto/s3transfer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "e570b74d01dc1ba0ef49ee008208bb320cccb574719829128aaabb0efaefff07"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
