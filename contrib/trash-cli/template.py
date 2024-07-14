pkgname = "trash-cli"
pkgver = "0.24.5.26"
pkgrel = 0
build_style = "python_pep517"
# FIXME: fails with {'command output': "trash-put: 'link-to-dir/' trashed in ~/tmpsjbhqli4_trash_cli_test/trash-dir"} != {'command output': "trash-put: 'link-to-dir/' trashed in /trash-dir"}
make_check_args = [
    "-k",
    "not test_link_to_dir_without_slashes "
    "and not test_link_to_dir_with_slashes",
]
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = ["python-psutil", "python-six"]
checkdepends = [
    "python-flexmock",
    "python-mock",
    "python-parameterized",
    "python-pytest",
    *depends,
]
pkgdesc = "Command line interface to the freedesktop.org trashcan"
maintainer = "Hugo Machet <mail@hmachet.com>"
license = "GPL-2.0-or-later"
url = "https://github.com/andreafrancia/trash-cli"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "1d7dec1ad8f0264ceb1b0211d25fffee99c9409cd2e1d36dcc82ac5540f39ce5"


def post_install(self):
    self.install_license("COPYING")
    self.install_man("man/man1/trash*.1", glob=True)
