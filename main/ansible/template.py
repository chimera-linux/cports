pkgname = "ansible"
pkgver = "11.6.0"
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
license = "GPL-3.0-or-later"
url = "https://ansible.com"
source = f"$(PYPI_SITE)/a/ansible/ansible-{pkgver}.tar.gz"
sha256 = "934a948caa3ec1a3eb277e7ab1638b808b074a6e0c46045794cde7b637e275d8"
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
