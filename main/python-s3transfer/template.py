pkgname = "python-s3transfer"
pkgver = "0.13.0"
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
sha256 = "27b51cd0c8464540ffcfc494eed977f702202f3f44ea5e56204175340a3ac95c"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
