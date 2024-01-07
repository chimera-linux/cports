# we need the undefs to avoid confusing the toolchain


def do_configure(self):
    cfgname = self.pkgname.removeprefix("u-boot-")
    self.do(
        "env",
        "-u",
        "CFLAGS",
        "-u",
        "CXXFLAGS",
        "-u",
        "CPPFLAGS",
        "-u",
        "LDFLAGS",
        "--",
        "gmake",
        f"{cfgname}_defconfig",
        f"CROSS_COMPILE={self.env['U_BOOT_TRIPLET']}-",
        f"CC={self.env['U_BOOT_TRIPLET']}-gcc",
        *self.configure_args,
    )


def do_build(self):
    self.do(
        "env",
        "-u",
        "CFLAGS",
        "-u",
        "CXXFLAGS",
        "-u",
        "CPPFLAGS",
        "-u",
        "LDFLAGS",
        "--",
        *self.make_build_wrapper,
        "gmake",
        f"-j{self.make_jobs}",
        f"EXTRAVERSION=-{self.pkgrel}",
        f"CROSS_COMPILE={self.env['U_BOOT_TRIPLET']}-",
        f"CC={self.env['U_BOOT_TRIPLET']}-gcc",
        *self.make_build_args,
    )


def do_check(self):
    pass


def do_install(self):
    destp = "usr/lib/u-boot/" + self.pkgname.removeprefix("u-boot-")
    for f in ["u-boot.bin", ".config"] + self.env["U_BOOT_TARGETS"].split():
        self.install_file(f, destp)
    # flasher
    if (self.files_path / "flash.sh").is_file():
        self.install_file(self.files_path / "flash.sh", destp, mode=0o755)
    # licenses
    for f in (self.cwd / "Licenses").iterdir():
        self.install_license(f"Licenses/{f.name}")


def use(tmpl):
    tmpl.do_configure = do_configure
    tmpl.do_build = do_build
    tmpl.do_check = do_check
    tmpl.do_install = do_install
