pkgname = "base-files"
_iana_ver = "20241220"
pkgver = f"0.1.{_iana_ver}"
pkgrel = 4
replaces = ["dinit-chimera<0.99.11-r2", "gcompat<1.1.0-r2"]
# highest priority dir owner
replaces_priority = 65535
pkgdesc = "Chimera Linux base system files"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"
# no tests
options = ["!check", "bootstrap", "keepempty", "brokenlinks"]


def install(self):
    # base root dirs
    for d in [
        "boot",
        "dev",
        "etc",
        "home",
        "media",
        "mnt",
        "proc",
        "run",
        "sys",
        "usr",
    ]:
        self.install_dir(d)

    # /usr dirs
    for d in ["bin", "include", "lib", "share", "src"]:
        self.install_dir("usr/" + d)
        self.install_dir("usr/local/" + d)

    # apk exec dir
    self.install_dir("usr/lib/apk/exec")

    # mandirs
    for i in range(1, 8):
        self.install_dir("usr/share/man/man" + str(i))

    # root's home dir
    self.install_dir("root")
    (self.destdir / "root").chmod(0o750)

    # /tmp
    self.install_dir("tmp")
    (self.destdir / "tmp").chmod(0o777)

    # Create bin and lib dirs and symlinks
    for d in ["bin", "lib"]:
        self.install_dir("usr/" + d)
        self.install_link(d, "usr/" + d)

    # Symlink sbin paths to /usr/bin
    self.install_link("sbin", "usr/bin")
    self.install_link("usr/sbin", "bin")
    self.install_link("usr/local/sbin", "bin")
    # wordsized stuff
    libwn = f"lib{self.profile().wordsize}"
    self.install_link(libwn, "lib")
    self.install_link(f"usr/{libwn}", "lib")
    self.install_link(f"usr/local/{libwn}", "lib")

    # Users and tmpfiles
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_tmpfiles(self.files_path / "tmp.conf", name="tmp")
    self.install_tmpfiles(self.files_path / "var.conf", name="var")

    # we need apk to install these for now to correctly populate the dbs
    self.install_file(self.files_path / "etc/group", "etc")
    self.install_file(self.files_path / "etc/passwd", "etc")

    # Mutable files not to be tracked by apk
    for f in [
        "fstab",
        "hosts",
        "issue",
        "nsswitch.conf",
        "profile",
        "profile.path",
    ]:
        self.install_file(self.files_path / "share" / f, "usr/share/base-files")

    self.install_file(
        self.files_path / "share/securetty", "usr/share/pam", mode=0o600
    )

    # Files that should not be changed
    for f in [
        "chimera-release",
        "os-release",
    ]:
        self.install_file(self.files_path / "lib" / f, "usr/lib")

    # Systemwide profile snippets
    for f in (self.files_path / "profile.d").glob("*.sh"):
        self.install_file(f, "usr/lib/profile.d")

    # Install common licenses
    self.install_dir("usr/share/licenses")

    for f in (self.files_path / "licenses").iterdir():
        self.install_file(f, "usr/share/licenses")

    self.install_bin(self.files_path / "lsb_release")

    # iana etc files
    for f in [
        "protocols",
        "services",
    ]:
        self.install_file(self.files_path / "iana" / f, "usr/share/iana")
