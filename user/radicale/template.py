pkgname = "radicale"
pkgver = "3.5.4"
pkgrel = 0
build_style = "python_pep517"
hostmakedepends = [
    "python-build",
    "python-installer",
    "python-setuptools",
    "python-wheel",
]
depends = [
    "python-argon2-cffi",
    "python-bcrypt",
    "python-defusexml",
    "python-ldap3",
    "python-passlib",
    "python-pika",
    "python-requests",
    "python-vobject",
]
checkdepends = [
    "python-pytest",
    "python-waitress",
    *depends,
]
pkgdesc = "CalDAV and CardDAV sync server"
license = "GPL-3.0-or-later"
url = "https://radicale.org"
source = f"https://github.com/Kozea/Radicale/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "dcbfb7ab0b2f89cab0f566ea179d768a5016597b0c1f177431a123de57509b3b"


def post_install(self):
    self.install_service("^/radicale")
    self.install_tmpfiles("^/tmpfiles.conf")
    self.install_sysusers("^/sysusers.conf")
    self.install_files("contrib", "usr/share/radicale")
    self.install_file("config", "usr/share/radicale")
    self.install_file("rights", "usr/share/radicale")
