import pathlib
from cbuild.core import chroot


def extract(self):
    self.cp(
        self.sources_path
        / f"{self.pkgname.removeprefix('ruby-')}-{self.pkgver}.gem",
        ".",
    )


def install(self):
    gemdir = pathlib.Path(
        chroot.enter(
            "gem",
            "env",
            "gemdir",
            capture_output=True,
            ro_root=True,
            ro_build=True,
            unshare_all=True,
            check=True,
        )
        .stdout.strip()
        .decode()
    ).relative_to("/")
    idir = gemdir / f"gems/{self.pkgname.removeprefix('ruby-')}-{self.pkgver}"

    self.do(
        "gem",
        "install",
        "--local",
        "--install-dir",
        self.chroot_destdir / gemdir,
        "--bindir",
        self.chroot_destdir / "usr/bin",
        "--ignore-dependencies",
        "--no-document",
        "--verbose",
        self.chroot_cwd
        / f"{self.pkgname.removeprefix('ruby-')}-{self.pkgver}.gem",
    )

    # cache
    self.rm(self.destdir / gemdir / "cache", recursive=True, force=True)

    # source/docs
    self.rm(self.destdir / idir / "ext", recursive=True, force=True)

    # installed tests, benchmarks etc
    for f in [
        "autotest",
        "benchmark",
        "benchmarks",
        "demo",
        "examples",
        "script",
        "test",
        "tests",
    ]:
        self.rm(self.destdir / idir / f, recursive=True, force=True)

    # files at gem root
    for f in (self.destdir / idir).iterdir():
        if not f.is_file():
            continue
        # TODO: make this flexible somehow
        if self._license_install and (
            f.name == "LICENSE" or f.name == "COPYING"
        ):
            self.install_license(f)
        f.unlink()

    # unnecessary files
    for f in (self.destdir / gemdir / "extensions").rglob("*"):
        if f.name == "mkmf.log" or f.name == "gem_make.out":
            f.unlink()

    # move manpages
    mdir = self.destdir / idir / "man"
    if mdir.is_dir():
        for f in mdir.rglob("*.[1-8]"):
            self.install_man(f)
        self.rm(mdir, recursive=True)

    # move executables if needed
    bdir = self.destdir / idir / "bin"
    if idir.is_dir():
        for f in idir.iterdir():
            self.install_bin(f)
        self.rm(bdir, recursive=True)

    # move config files if needed
    edir = self.destdir / idir / "etc"
    if edir.is_dir():
        self.install_dir("etc")
        for e in edir.iterdir():
            self.mv(e, self.destdir / "etc")


def use(tmpl):
    tmpl.extract = extract
    tmpl.install = install
