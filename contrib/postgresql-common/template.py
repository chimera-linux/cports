pkgname = "postgresql-common"
pkgver = "1.2"
pkgrel = 0
triggers = ["/usr/libexec/postgresql*", "/usr/share/postgresql*"]
pkgdesc = "Common files for PostgreSQL"
maintainer = "mia <mia@mia.jetzt>"
license = "MIT"
url = "https://www.postgresql.org"
options = ["!distlicense"]


def do_install(self):
    self.install_bin(self.files_path / "pg_versions")
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="postgresql.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="postgresql.conf",
    )


# TODO: dinit service
