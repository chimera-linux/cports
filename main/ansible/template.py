pkgname = "ansible"
pkgver = "10.4.0"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
]
depends = ["ansible-core"]
checkdepends = [
    "python-pytest",
    "python-pytest-mock",
    "python-pytest-xdist",
    *depends,
]
pkgdesc = "Configuration management and multinode orchestration framework"
maintainer = "Mara <177581589+catgirlconspiracy@users.noreply.github.com>"
license = "GPL-3.0-or-later"
url = "https://ansible.com"
source = f"$(PYPI_SITE)/a/ansible/ansible-{pkgver}.tar.gz"
sha256 = "5c12048831a6690fc865dfe03dc8ab61c3ba08b5d01b249a16b247ad99a60bc0"
# many collections either require additional Python modules, or the tests
# require dependencies that aren't in the tarball, or they're just broken
# (possibly due to Python version compat issues)
options = ["!check"]


def check(self):
    for collection_dir in self.find("ansible_collections", "*/*/tests/unit"):
        collection_dir = collection_dir.parent.parent
        print(f"checking {collection_dir}")
        self.do(
            "ansible-test",
            "units",
            wrksrc=self.chroot_cwd / collection_dir,
        )
