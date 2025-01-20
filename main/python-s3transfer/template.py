pkgname = "python-s3transfer"
pkgver = "0.11.1"
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
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/s3transfer"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "b22725ab2fbcc236b937cf86d31e9cd5b7d20e367991531679886eb2502fa9f7"


def init_check(self):
    self.make_check_args += [f"--numprocesses={self.make_jobs}"]
