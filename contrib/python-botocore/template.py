pkgname = "python-botocore"
pkgver = "1.34.125"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-dateutil",
    "python-jmespath",
    "python-urllib3",
]
checkdepends = depends + ["python-pytest"]
pkgdesc = "Core module supporting boto3 and aws cli"
maintainer = "ttyyls <contact@behri.org>"
license = "Apache-2.0"
url = "https://github.com/boto/botocore"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "5e6762287e78a3ba905c1cc1ac8b705b768008497c70863e378ade4f0f9bbe44"
# takes forever
options = ["!check"]
