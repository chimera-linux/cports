pkgname = "base-files"
pkgver = "0.2"
pkgrel = 1
_netbase_ver = "6.5"
replaces = ["dinit-chimera<0.99.11-r2", "gcompat<1.1.0-r2"]
# highest priority dir owner
replaces_priority = 65535
pkgdesc = "Chimera Linux base system files"
license = "custom:meta"
url = "https://chimera-linux.org"
# netbase files from debian; iana does not provide aliases
# which e.g. breaks rpcbind (which assumes "portmapper" service
# which should be an alias of "sunrpc" but is not in iana files)
source = [
    f"!https://salsa.debian.org/md/netbase/-/raw/v{_netbase_ver}/etc/protocols>protocols-{_netbase_ver}",
    f"!https://salsa.debian.org/md/netbase/-/raw/v{_netbase_ver}/etc/services>services-{_netbase_ver}",
]
sha256 = [
    "4959498abbadaa1e50894a266f8d0d94500101cfe5b5f09dcad82e9d5bdfab46",
    "20c48954659cf753baa383ecde0e6f026fadc06c2c9fbe29d88d928188c3ec17",
]
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

    # files from debian netbase
    for f in [
        "protocols",
        "services",
    ]:
        self.install_file(
            self.sources_path / f"{f}-{_netbase_ver}",
            "usr/share/netbase",
            name=f,
        )
