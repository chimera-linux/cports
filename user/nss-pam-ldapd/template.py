pkgname = "nss-pam-ldapd"
pkgver = "0.9.13"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-pynslcd",
    "--disable-utils",
    "--with-ldap-lib=openldap",
    "--with-nslcd-pidfile=/run/nslcd/nslcd.pid",
    "--with-nslcd-socket=/run/nslcd/socket",
    "--with-pam-seclib-dir=/usr/lib/security",
]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = [
    "dinit-chimera",
    "linux-pam-devel",
    "musl-nscd",
    "openldap-devel",
]
depends = ["musl-nscd"]
pkgdesc = "NSS and PAM modules and daemon for LDAP directories"
license = "LGPL-2.1-or-later"
url = "https://arthurdejong.org/nss-pam-ldapd"
source = f"{url}/nss-pam-ldapd-{pkgver}.tar.gz"
sha256 = "e01784e17cb533bb66bd0601e205e785263445c3c2df7a6f90232ab4131c716d"
# tests need a running ldap server and nslcd
options = ["!check"]


def post_install(self):
    # empty, config is installed in usr/share/etc
    self.uninstall("etc")
    self.install_license("COPYING")
    conf = self.cwd / "nslcd.conf"
    conf.write_text(
        conf.read_text()
        .replace("uid nslcd", "uid _nslcd")
        .replace("gid nslcd", "gid _nslcd")
    )
    self.install_file(conf, "usr/share/etc", mode=0o600)
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "nslcd")
