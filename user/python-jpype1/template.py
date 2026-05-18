pkgname = "python-jpype1"
pkgver = "1.7.1"
pkgrel = 0
build_style = "python_pep517"
make_env = {"JAVA_HOME": "/usr/lib/jvm/java-21-openjdk"}
hostmakedepends = [
    "apache-ant",
    "cmake",
    "ninja",
    "python-build",
    "python-installer",
    "python-scikit_build_core",
]
makedepends = [
    "openjdk21-jdk",
    "python-devel",
]
depends = [
    "python",
    "python-packaging",
]
pkgdesc = "Python to Java bridge"
license = "Apache-2.0"
url = "https://www.jpype.org"
source = f"$(PYPI_SITE)/j/jpype1/jpype1-{pkgver}.tar.gz"
sha256 = "3cd88838dc3d2d546f7eaeadaaff864e590010c15f2b6a44b6f37e60796a14b2"
# requires a running JVM and complex setup in container
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
