pkgname = "os-prober"
pkgver = "1.81"
pkgrel = 1
pkgdesc = "Utility to detect other OSes on a set of drives"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://tracker.debian.org/pkg/os-prober"
source = f"$(DEBIAN_SITE)/main/o/{pkgname}/{pkgname}_{pkgver}.tar.xz"
sha256 = "2fd928ec86538227711e2adf49cfd6a1ef74f6bb3555c5dad4e0425ccd978883"

# only x86 and aarch64 hooks are useful to us
match self.profile().arch:
    case "x86_64":
        _arch = "x86"
    case "aarch64":
        _arch = "arm64"
    case _:
        _arch = None


def do_build(self):
    from cbuild.util import compiler

    compiler.C(self).invoke(["newns.c"], "newns")


def do_install(self):
    self.install_bin("linux-boot-prober")
    self.install_bin("os-prober")

    self.install_file(self.files_path / "os-prober.conf", "usr/lib/tmpfiles.d")

    self.install_file("newns", "usr/lib/os-prober", mode=0o755)
    self.install_file("common.sh", "usr/share/os-prober", mode=0o755)

    for d in [
        "os-probes",
        "os-probes/mounted",
        "os-probes/init",
        "linux-boot-probes",
        "linux-boot-probes/mounted",
    ]:
        # common scripts
        for f in (self.cwd / f"{d}/common").glob("*"):
            self.install_file(f, f"usr/lib/{d}", mode=0o755)
        # arch scripts
        if not _arch or not (self.cwd / f"{d}/{_arch}").is_dir():
            continue
        for f in (self.cwd / f"{d}/{_arch}").glob("*"):
            self.cp(f, self.destdir / f"usr/lib/{d}", recursive=True)

    # macos probe
    if _arch == "x86":
        self.install_file(
            "os-probes/mounted/powerpc/20macosx",
            "usr/lib/os-probes/mounted",
            mode=0o755,
        )
