# we need the undefs to avoid confusing the toolchain


def configure(self):
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
        "make",
        f"{cfgname}_defconfig",
        f"CROSS_COMPILE={self.env['U_BOOT_TRIPLET']}-",
        f"CC={self.env['U_BOOT_TRIPLET']}-gcc",
        *self.configure_args,
    )


def build(self):
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
        "make",
        f"-j{self.make_jobs}",
        f"EXTRAVERSION=-{self.pkgrel}",
        f"CROSS_COMPILE={self.env['U_BOOT_TRIPLET']}-",
        f"CC={self.env['U_BOOT_TRIPLET']}-gcc",
        *self.make_build_args,
    )


def check(self):
    pass


_flash_scr = """#!/bin/sh

DEVICE=$1
UBPATH=$2

[ -n "$DEVICE" -a -n "$UBPATH" ] || exit 32
[ -b "$DEVICE" ] || exit 33
"""


def install(self):
    destp = "usr/lib/u-boot/" + self.pkgname.removeprefix("u-boot-")
    for f in ["u-boot.bin", ".config"]:
        self.install_file(f, destp)
    # explicit targets
    foffs = []
    if "U_BOOT_TARGETS" in self.env:
        tgts = self.env["U_BOOT_TARGETS"].split()
        for f in tgts:
            tf = f.split(":")
            if len(tf) == 2:
                foffs.append(tf)
                self.install_file(tf[0], destp)
            else:
                self.install_file(f, destp)
    # flasher if explicitly present, or generate if needed
    if (self.files_path / "flash.sh").is_file():
        self.install_file(self.files_path / "flash.sh", destp, mode=0o755)
    elif len(foffs) > 0:
        with open(self.destdir / destp / "flash.sh", "w") as outf:
            outf.write(_flash_scr)
            for fn, off in foffs:
                outf.write(f"""[ -r "${{UBPATH}}/{fn}" ] || exit 34\n""")
            outf.write("\n")
            for fn, off in foffs:
                outf.write(
                    f"""dd if="${{UBPATH}}/{fn}" of="${{DEVICE}}" seek={off} conv=notrunc,fsync || exit 35\n"""
                )
        (self.destdir / destp / "flash.sh").chmod(0o755)
    # licenses
    for f in (self.cwd / "Licenses").iterdir():
        self.install_license(f"Licenses/{f.name}")


def use(tmpl):
    tmpl.configure = configure
    tmpl.build = build
    tmpl.check = check
    tmpl.install = install
